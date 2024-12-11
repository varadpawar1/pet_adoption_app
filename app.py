from flask import Flask, flash
from flask import render_template
from flask import request,session, redirect,send_from_directory,make_response 
from flask_session import Session
from datetime import timedelta
from datetime import datetime
import redis
import sys
import os
import matplotlib.pyplot as plt
import io
import base64
import os
import sys


# Get the root directory of the project (assumes this script is in the root directory or a subfolder)
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

# Define session directory relative to the project root
session_dir = os.path.join(project_root, 'flask_session')

# Create session directory if it doesn't exist
if not os.path.exists(session_dir):
    os.makedirs(session_dir)

# Print the paths for debugging
print(f"Project root: {project_root}")
# print(f"Session directory: {session_dir}")

import matplotlib.pyplot as plt
import io
import base64

from models.user import user
from models.pet import pet
from models.shelter import shelter
from models.adoption import adoption
from models.appointment import appointment
import time
import pymysql
from flask import g, Flask, request, session, redirect, flash
from datetime import datetime
import yaml


#create Flask app instance
app = Flask(__name__,static_url_path='')
# app.config['SESSION_FILE_DIR'] = session_dir
# app.config['SESSION_TYPE'] = 'filesystem'

# from cachelib.file import FileSystemCache
# import os

# class GracefulFileSystemCache(FileSystemCache):
#     def _run_safely(self, fn, *args, **kwargs):
#         try:
#             return fn(*args, **kwargs)
#         except FileNotFoundError:
#             # Handle the missing file gracefully
#             return None

# # Update Flask's session cache
# app.session_interface.cache = GracefulFileSystemCache(
#     cache_dir="g:\\My Drive\\Data Driven Application\\pet_adoption_app\\flask_session"
# )
# app.config['SESSION_TYPE'] = 'sqlalchemy'
# app.config['SESSION_SQLALCHEMY'] = 'sqlite:///sessions.db'
# Session(app)
# import shutil

# session_dir = "g:\\My Drive\\Data Driven Application\\pet_adoption_app\\flask_session"
# shutil.rmtree(session_dir)
# os.makedirs(session_dir)  # Recreate the directory

# # Redis configuration
# app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_USE_SIGNER'] = True
# app.config['SESSION_KEY_PREFIX'] = 'flask_session:'
# app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379)

# Initialize the session
# Session(app)
# Load configuration
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

db_config = config['db']

# Database connection function
def get_db_connection():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['passwd'],
            database=db_config['db'],
            port=db_config['port']
        )
    return g.db

# Teardown function to close DB connection
@app.teardown_appcontext
def close_db_connection(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
#create Flask app instance
app = Flask(__name__,static_url_path='')

#Configure serverside sessions 
app.config['SECRET_KEY'] = '56hdtryhRTg'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
sess = Session()
sess.init_app(app)

#Basic root route - show the word 'homepage'
@app.route('/')  #route name
def home(): #view function
    return render_template('homepage.html')


@app.context_processor
def inject_user():
    return dict(me=session.get('user'))

'''
- DDL (init) script
- MyISAM engine
- no referential integrity in create statement

TODO:
-show login form
-check login on submit
    -set session if login ok
-redirect to menu
-check session on login required pages
'''
def checkSession():
    timeout = 3600  # Session timeout in seconds (e.g., 1 hour)
    active_time = session.get('active', 0)
    current_time = time.time()
    time_difference = current_time - active_time

    print(f"Session active timestamp: {active_time}")
    print(f"Current time: {current_time}")
    print(f"Time difference: {time_difference}")

    if time_difference > timeout:
        print("Session expired.")
        session['msg'] = 'Your session has timed out.'
        return False

    # Update session active time to extend session
    session['active'] = current_time
    print("Session is valid. Updating active timestamp.")
    return True

@app.before_request
def update_active_session():
    if session.get('user'):
        session['active'] = time.time()


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    # If user is already logged in, redirect to the main page
    if session.get('user'):
        return redirect('/main')
    u = user()  # Assuming `user` is the model class for managing users

    if request.method == 'POST':
        # Collect form data
        data = {field: request.form.get(field) for field in [
            'email', 'password', 'password2', 'name', 'phone_number', 'Address', 'zipcode', 'user_type', 'shelter_id']}
        
        # Add the registration date (current date)
        data['registration_date'] = datetime.now().strftime('%Y-%m-%d')
        data['user_type'] = 'customer'
        # Handle shelter_id based on user_type
        if data['user_type'] == 'admin':
            if not data['shelter_id']:  # Check if shelter_id is provided
                u.errors.append('Shelter ID is required for admin users.')
        else:
            data['shelter_id'] = None  # Nullify shelter_id for non-admin users

        u.set(data)  # Set data in the user object
        
        # Validate and create the account
        if u.verify_new():  # Assuming `verify_new` validates the user data
            u.insert()  # Insert into the database
            return redirect('/login')  # Redirect to login after successful account creation
        else:
            # Render the form with errors if validation fails
            return render_template('create_account.html', obj=u)

    # Initialize empty form data
    u.data = [{
        'email': '', 'password': '', 'password2': '', 'name': '', 'phone_number': '',
        'Address': '', 'zipcode': '', 'user_type': 'customer', 'shelter_id': '', 'registration_date': datetime.now().strftime('%Y-%m-%d')
    }]
    return render_template('create_account.html', obj=u)




@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect to the main page
    if session.get('user'):
        return redirect('/main')

    # Handle POST request for login
    if request.method == 'POST' and request.form.get('name') and request.form.get('password'):
        u = user()
        if u.tryLogin(request.form.get('name'), request.form.get('password')):
            print("Login ok")
            session['user'] = u.data[0]  # Store user information in session
            session['active'] = time.time()  # Set session active time
            return redirect('/main')
        else:
            print("Login Failed")
            return render_template('login.html', title='Login', msg='Incorrect username or password.')

    # Handle GET request or incomplete POST
    msg = session.pop('msg', 'Type your email and password to continue.')
    return render_template('login.html', title='Login', msg=msg)
  
    
# @app.route('/logout',methods = ['GET','POST'])
# def logout():
#         # If user is already logged in, redirect to the main page
#     if session.get('user'):
#         return redirect('/main')
#     if session.get('user') is not None:
#         del session['user']
#         del session['active']
#     return render_template('login.html', title='Login', msg='You have logged out.')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('user'):
        print("Logging out user:", session['user'])
        session.clear()
        print("Session cleared.")

    print("Redirecting to /login.")
    return redirect('/login')



@app.route('/main')
def main():
    print("Accessing /main route. Session data:", session)

    # Ensure user is logged in
    if not session.get('user'):
        print("No user in session. Redirecting to /login.")
        return redirect('/login')

    # Validate session
    if not checkSession():
        print("Session validation failed. Redirecting to /login.")
        return redirect('/login')

    # Admin: Render admin main menu
    if session['user']['user_type'] == 'admin':
        print("Rendering admin main menu.")
        return render_template('main.html', title='Main menu')

    # Customer: Fetch shelters and available pets
    elif session['user']['user_type'] == 'customer':
        print("Rendering customer main menu.")
        
        # Fetch all shelters
        shelter_obj = shelter()
        shelter_obj.cur.execute("SELECT * FROM VB_Shelters")
        shelters = shelter_obj.cur.fetchall()
        print("Shelters fetched:", shelters)

        # Fetch all available pets
        pet_obj = pet()
        pet_obj.cur.execute("SELECT * FROM VB_Pets WHERE status = 'Available'")
        pets = pet_obj.cur.fetchall()
        print("Pets fetched:", pets)

        return render_template('customer_main.html', shelters=shelters, pets=pets)

    # Redirect unknown user types to login
    else:
        print("Unknown user type. Redirecting to /login.")
        return redirect('/login')


@app.route('/insights')
def insights():
    print("Accessing /insights route.")

    # Ensure user is logged in and is an admin
    if not session.get('user') or session['user']['user_type'] != 'admin':
        return redirect('/login')

    pet_obj = pet()
    shelter_obj = shelter()

    # --- Pets by Age Group ---
    pet_obj.cur.execute("""
        SELECT
            CASE
                WHEN age < 1 THEN '0-1 years'
                WHEN age BETWEEN 1 AND 3 THEN '1-3 years'
                ELSE '3+ years'
            END as age_group,
            COUNT(*) as count
        FROM VB_Pets
        GROUP BY age_group;
    """)
    age_groups = pet_obj.cur.fetchall()
    age_group_labels = [row['age_group'] for row in age_groups]
    age_group_counts = [row['count'] for row in age_groups]

    plt.figure(figsize=(6, 4))
    plt.bar(age_group_labels, age_group_counts, color=['#ff9999', '#66b3ff', '#99ff99'])
    plt.xlabel('Age Group')
    plt.ylabel('Number of Pets')
    plt.title('Pets by Age Group')
    plt.tight_layout()
    img_age = io.BytesIO()
    plt.savefig(img_age, format='png')
    img_age.seek(0)
    age_group_graph = base64.b64encode(img_age.getvalue()).decode('utf-8')
    plt.close()

    # --- Gender Distribution of Pets ---
    pet_obj.cur.execute("""
        SELECT gender, COUNT(*) as count
        FROM VB_Pets
        GROUP BY gender;
    """)
    gender_data = pet_obj.cur.fetchall()
    gender_labels = [row['gender'] for row in gender_data]
    gender_counts = [row['count'] for row in gender_data]

    plt.figure(figsize=(6, 4))
    plt.pie(gender_counts, labels=gender_labels, autopct='%1.1f%%', colors=['#ffcccb', '#add8e6'])
    plt.title('Gender Distribution of Pets')
    plt.tight_layout()
    img_gender = io.BytesIO()
    plt.savefig(img_gender, format='png')
    img_gender.seek(0)
    gender_distribution_graph = base64.b64encode(img_gender.getvalue()).decode('utf-8')
    plt.close()

    # --- Shelters vs. Pet Count ---
    shelter_obj.cur.execute("""
        SELECT s.shelter_name as shelter_name, COUNT(p.pet_id) as pet_count
        FROM VB_Shelters s
        JOIN VB_Pets p ON s.shelter_id = p.shelter_id
        GROUP BY s.shelter_name;
    """)
    shelter_data = shelter_obj.cur.fetchall()
    shelter_names = [row['shelter_name'] for row in shelter_data]
    pet_counts = [row['pet_count'] for row in shelter_data]

    plt.figure(figsize=(8, 5))
    plt.bar(shelter_names, pet_counts, color='#ffcc99')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Shelters')
    plt.ylabel('Number of Pets')
    plt.title('Shelters vs. Pet Count')
    plt.tight_layout()
    img_shelter = io.BytesIO()
    plt.savefig(img_shelter, format='png')
    img_shelter.seek(0)
    shelter_graph = base64.b64encode(img_shelter.getvalue()).decode('utf-8')
    plt.close()

    # --- Pets vs. Breed ---
    pet_obj.cur.execute("""
        SELECT breed, COUNT(*) as count
        FROM VB_Pets
        GROUP BY breed
        ORDER BY count DESC
        LIMIT 10;
    """)
    breed_data = pet_obj.cur.fetchall()
    breed_names = [row['breed'] for row in breed_data]
    breed_counts = [row['count'] for row in breed_data]

    plt.figure(figsize=(8, 5))
    plt.bar(breed_names, breed_counts, color='#99c2ff')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Breed')
    plt.ylabel('Number of Pets')
    plt.title('Top 10 Breeds by Pet Count')
    plt.tight_layout()
    img_breed = io.BytesIO()
    plt.savefig(img_breed, format='png')
    img_breed.seek(0)
    breed_graph = base64.b64encode(img_breed.getvalue()).decode('utf-8')
    plt.close()

    return render_template(
        'insights.html',
        age_group_graph=age_group_graph,
        gender_distribution_graph=gender_distribution_graph,
        shelter_graph=shelter_graph,
        breed_graph=breed_graph
    )


@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    if not session.get('user'):
        return redirect('/login')

    # Get form data
    shelter_id = request.form['shelter_id']
    pet_id = request.form['pet_id']
    user_id = session['user']['user_id']
    appointment_date = datetime.now()

    # Insert into VB_Appointments
    query = """
        INSERT INTO VB_Appointments (appointment_date, status, shelter_id, user_id)
        VALUES (%s, %s, %s, %s)
    """
    values = (appointment_date, 'Scheduled', shelter_id, user_id)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()

    flash(f"Appointment for pet ID {pet_id} successfully booked!", "success")
    return redirect('/main')

@app.route('/adopt', methods=['POST'])
def adopt_pet():
    if not session.get('user'):
        return redirect('/login')

    try:
        # Get form data
        pet_id = request.form['pet_id']
        user_id = session['user']['user_id']
        request_date = datetime.now()

        # Insert into VB_Adoptions
        query = """
            INSERT INTO VB_Adoptions (request_date, status, user_id, pet_id)
            VALUES (%s, %s, %s, %s)
        """
        values = (request_date, 'Pending', user_id, pet_id)

        # Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

        # Notify user of success
        flash(f"Adoption request for pet ID {pet_id} successfully submitted!", "success")
        return redirect('/main')

    except Exception as e:
        # Handle errors and notify the user
        print(f"Error while processing adoption: {e}")
        flash("An error occurred while submitting your adoption request. Please try again.", "error")
        return redirect('/main')



@app.route('/shelter/<int:shelter_id>')
def shelter_pets(shelter_id):
    if not session.get('user') or session['user']['user_type'] != 'customer':
        return redirect('/login')

    try:
        # Fetch shelter details
        shelter_obj = shelter()  # Assuming `shelter` is the model for VB_Shelters
        shelter_obj.cur.execute("SELECT * FROM VB_Shelters WHERE shelter_id = %s", (shelter_id,))
        shelter_data = shelter_obj.cur.fetchone()  # Retrieve specific shelter
        if not shelter_data:
            flash("Shelter not found.", "error")
            return redirect('/main')

        print("Shelter fetched:", shelter_data)

        # Fetch pets for this shelter
        pet_obj = pet()  # Assuming `pet` is the model for VB_Pets
        pet_obj.cur.execute(
            "SELECT * FROM VB_Pets WHERE status = 'Available' AND shelter_id = %s",
            (shelter_id,)
        )
        pets = pet_obj.cur.fetchall()  # Retrieve pets for the shelter
        print("Pets fetched for shelter:", pets)

        return render_template('shelter_pets.html', shelter=shelter_data, pets=pets)

    except Exception as e:
        print("Error fetching shelter or pets:", e)
        flash("An error occurred while fetching shelter details.", "error")
        return redirect('/main')



    
@app.route('/users/manage', methods=['GET', 'POST'])
def manage_user():
    # Ensure the user is logged in and is an admin
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    u = user()
    action = request.args.get('action', 'list')  # Default action is 'list'
    pkval = request.args.get('pkval')  # Primary key value (user_id)

    # List Users
    if action == 'list':
        u.getAll()
        return render_template('users_list.html', users=u.data)

    # Add New User
    if action == 'new':
        if request.method == 'POST':
            # Collect form data
            data = {field: request.form.get(field) for field in [
                'email', 'password', 'password2', 'phone_number', 'registration_date',
                'Address', 'zipcode', 'name', 'user_type', 'shelter_id']}
            u.set(data)
            if u.verify_new():
                u.insert()
                return redirect('/users/manage?action=list')  # Redirect to the list view
            return render_template('users_add.html', obj=u)  # Show errors if validation fails
        return render_template('users_add.html', obj=u)  # Render form for new user

    # Edit User
    if action == 'edit':
        u.getById(pkval)
        if not u.data:
            return "User not found", 404
        if request.method == 'POST':
            # Update data
            updated_data = {field: request.form.get(field) for field in [
                'email', 'password', 'password2', 'phone_number', 'registration_date',
                'Address', 'zipcode', 'name', 'user_type', 'shelter_id']}
            u.data[0].update(updated_data)
            if u.verify_update():
                u.update()
                return redirect('/users/manage?action=list')  # Redirect to the list view
            return render_template('users_edit.html', obj=u)  # Show errors if validation fails
        return render_template('users_edit.html', obj=u)  # Render form for editing

    # Delete User
    if action == 'delete' and pkval:
        u.deleteById(pkval)
        return redirect('/users/manage?action=list')  # Redirect to the list view after deletion

    return "Invalid action", 400  # Handle invalid actions



@app.route('/pets/manage', methods=['GET', 'POST'])
def manage_pet():
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    p = pet()  # Assuming `pet` is the model class for managing pets
    s = shelter()
    action = request.args.get('action', 'list')  # Default action is 'list'
    pkval = request.args.get('pkval')  # Primary key value (pet_id)

    # List Pets
    if action == 'list':
        p.getAll()
        s.getAll()
        return render_template('pets_list.html', pets=p.data, shelters= s.data)

    # Add New Pet
    if action == 'new':
        if request.method == 'POST':
            # Collect form data
            data = {field: request.form.get(field) for field in [
                'name', 'type', 'breed', 'age', 'gender', 'health_status',
                'description', 'image_url', 'listing_date', 'status', 'shelter_id']}
            p.set(data)
            if p.verify_new():
                p.insert()
                return redirect('/pets/manage?action=list')  # Redirect to the list view
            return render_template('pets_add.html', obj=p)  # Show errors if validation fails
        # Initialize empty data for the form
        p.data = [{'name': '', 'type': '', 'breed': '', 'age': '', 'gender': '', 'health_status': '',
                   'description': '', 'image_url': '', 'listing_date': '', 'status': '', 'shelter_id': ''}]
        return render_template('pets_add.html', obj=p)

    # Edit Pet
    if action == 'edit':
        p.getById(pkval)
        if not p.data:
            return "Pet not found", 404
        if request.method == 'POST':
            # Update data
            updated_data = {field: request.form.get(field) for field in [
                'name', 'type', 'breed', 'age', 'gender', 'health_status',
                'description', 'image_url', 'listing_date', 'status', 'shelter_id']}
            p.data[0].update(updated_data)
            if p.verify_update():
                p.update()
                return redirect('/pets/manage?action=list')  # Redirect to the list view
            return render_template('pets_edit.html', obj=p)  # Show errors if validation fails
        return render_template('pets_edit.html', obj=p)

    # Delete Pet
    if action == 'delete' and pkval:
        p.deleteById(pkval)
        return redirect('/pets/manage?action=list')  # Redirect to the list view after deletion

    return "Invalid action", 400  # Handle invalid actions



@app.route('/shelters/manage', methods=['GET', 'POST'])
def manage_shelter():
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    s = shelter()  # Assuming `shelter` is the model class for managing shelters
    action = request.args.get('action', 'list')  # Default action is 'list'
    pkval = request.args.get('pkval')  # Primary key value (shelter_id)

    # List Shelters
    if action == 'list':
        s.getAll()
        return render_template('shelters_list.html', shelters=s.data)

    # Add New Shelter
    if action == 'new':
        if request.method == 'POST':
            # Collect form data
            data = {field: request.form.get(field) for field in ['shelter_name', 'address', 'contact', 'website_url']}
            s.set(data)
            if s.verify_new():
                s.insert()
                return redirect('/shelters/manage?action=list')  # Redirect to the list view
            return render_template('shelters_add.html', obj=s)  # Show errors if validation fails
        # Initialize empty data for the form
        s.data = [{'shelter_name': '', 'address': '', 'contact': '', 'website_url': ''}]
        return render_template('shelters_add.html', obj=s)

    # Edit Shelter
    if action == 'edit':
        s.getById(pkval)
        if not s.data:
            return "Shelter not found", 404
        if request.method == 'POST':
            # Update data
            updated_data = {field: request.form.get(field) for field in ['shelter_name', 'address', 'contact', 'website_url']}
            s.data[0].update(updated_data)
            if s.verify_update():
                s.update()
                return redirect('/shelters/manage?action=list')  # Redirect to the list view
            return render_template('shelters_edit.html', obj=s)  # Show errors if validation fails
        return render_template('shelters_edit.html', obj=s)

    # Delete Shelter
    if action == 'delete' and pkval:
        s.deleteById(pkval)
        return redirect('/shelters/manage?action=list')  # Redirect to the list view after deletion

    return "Invalid action", 400  # Handle invalid actions


@app.route('/adoptions/manage', methods=['GET', 'POST'])
def manage_adoption():
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    a = adoption()  # Assuming `adoption` is the model class for managing adoptions
    u = user()
    p = pet()
    action = request.args.get('action', 'list')  # Default action is 'list'
    pkval = request.args.get('pkval')  # Primary key value (adoption_id)

    # List Adoptions
    if action == 'list':
        a.getAll()
        p.getAll()
        u.getAll()
        return render_template('adoptions_list.html', adoptions=a.data, pets=p.data, users=u.data)

        # Add New Adoption
    if action == 'new':
        if request.method == 'POST':
            # Collect form data
            data = {field: request.form.get(field) for field in ['request_date', 'status', 'adoption_date', 'user_id', 'pet_id']}
            
            # Convert empty adoption_date to None (NULL in the database)
            if not data['adoption_date']:
                data['adoption_date'] = None
            
            # Ensure request_date is properly formatted or defaults to today's date
            if not data['request_date']:
                data['request_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Set the data for validation and insertion
            a.set(data)
            if a.verify_new():
                a.insert()
                return redirect('/adoptions/manage?action=list')  # Redirect to the list view

            # Render the form with errors if validation fails
            return render_template('adoptions_add.html', obj=a)
        
        # Initialize default data for the form
        a.data = [{
            'request_date': datetime.now().strftime('%Y-%m-%d'),  # Default to today's date
            'status': 'Pending',  # Default status is Pending
            'adoption_date': None,  # Default to NULL
            'user_name': '',  # No default user ID
            'pet_name': ''  # No default pet ID
        }]
        return render_template('adoptions_add.html', obj=a)


    # Edit Adoption
    if action == 'edit':
        a.getById(pkval)
        if not a.data:
            return "Adoption not found", 404
        if request.method == 'POST':
            # Update data
            updated_data = {field: request.form.get(field) for field in ['request_date', 'status', 'adoption_date', 'user_id', 'pet_id']}
            a.data[0].update(updated_data)
            if a.verify_update():
                a.update()
                return redirect('/adoptions/manage?action=list')  # Redirect to the list view
            return render_template('adoptions_edit.html', obj=a)  # Show errors if validation fails
        return render_template('adoptions_edit.html', obj=a)

    # Delete Adoption
    if action == 'delete' and pkval:
        a.deleteById(pkval)
        return redirect('/adoptions/manage?action=list')  # Redirect to the list view after deletion

    return "Invalid action", 400  # Handle invalid actions


@app.route('/appointments/manage', methods=['GET', 'POST'])
def manage_appointment():
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    appt = appointment()  # Assuming `appointment` is the model class for managing appointments
    s = shelter()
    u = user()
    action = request.args.get('action', 'list')  # Default action is 'list'
    pkval = request.args.get('pkval')  # Primary key value (appointment_id)

    # List Appointments
    if action == 'list':
        appt.getAll()
        u.getAll()
        s.getAll()
        return render_template('appointments_list.html', appointments=appt.data, users=u.data, shelters=s.data)

    # Add New Appointment
    if action == 'new':
        if request.method == 'POST':
            # Collect form data
            data = {field: request.form.get(field) for field in ['appointment_date', 'status', 'shelter_id', 'user_id']}
            appt.set(data)
            if appt.verify_new():
                appt.insert()
                return redirect('/appointments/manage?action=list')  # Redirect to the list view
            return render_template('appointments_add.html', obj=appt)  # Show errors if validation fails
        # Initialize default data for the form
        appt.data = [{
            'appointment_date': datetime.now().strftime('%Y-%m-%d'),  # Default to today's date
            'status': 'Scheduled',  # Default status is Scheduled
            'shelter_id': '',  # No default shelter ID
            'user_id': ''  # No default user ID
        }]
        return render_template('appointments_add.html', obj=appt)

    # Edit Appointment
    if action == 'edit':
        appt.getById(pkval)
        if not appt.data:
            return "Appointment not found", 404
        if request.method == 'POST':
            # Update data
            updated_data = {field: request.form.get(field) for field in ['appointment_date', 'status', 'shelter_id', 'user_id']}
            appt.data[0].update(updated_data)
            if appt.verify_update():
                appt.update()
                return redirect('/appointments/manage?action=list')  # Redirect to the list view
            return render_template('appointments_edit.html', obj=appt)  # Show errors if validation fails
        return render_template('appointments_edit.html', obj=appt)

    # Delete Appointment
    if action == 'delete' and pkval:
        appt.deleteById(pkval)
        return redirect('/appointments/manage?action=list')  # Redirect to the list view after deletion

    return "Invalid action", 400  # Handle invalid actions


# endpoint route for static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# #standalone function to be called when we need to check if a user is logged in.
# def checkSession():
#     if 'active' in session.keys():
#         timeSinceAct = time.time() - session['active']
#         print(timeSinceAct)
#         if timeSinceAct > 500:
#             session['msg'] = 'Your session has timed out.'
#             return False
#         else:
#             session['active'] = time.time()
#             return True
#     else:
#         return False      
  
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug=True)   