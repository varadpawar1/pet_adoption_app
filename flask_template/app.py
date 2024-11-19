from flask import Flask
from flask import render_template
from flask import request,session, redirect,send_from_directory,make_response 
from flask_session import Session
from datetime import timedelta
import sys
sys.path.append('G:\My Drive\Data Driven Application\Project_Pet')

from user import user
from pet import pet
import time
import datetime

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
@app.route('/create_account',methods = ['GET','POST'])
def create_account():
    u = user()
    return u.hashPassword(request.args.get('pw'))

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.form.get('name') is not None and request.form.get('password') is not None:
        u = user()
        if u.tryLogin(request.form.get('name'),request.form.get('password')):
            print("Login ok")
            session['user'] = u.data[0]
            session['active'] = time.time()
            return redirect('main')
        else:
            print("Login Failed")
            return render_template('login.html', title='Login', msg='Incorrect username or password.')
    else:   
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your email and password to continue.'
        else:
            m = session['msg']
            session['msg'] = None
        return render_template('login.html', title='Login', msg=m)    
    
@app.route('/logout',methods = ['GET','POST'])
def logout():
    if session.get('user') is not None:
        del session['user']
        del session['active']
    return render_template('login.html', title='Login', msg='You have logged out.')

@app.route('/main')
def main():
    if checkSession() == False: 
        return redirect('/login')
    if session['user']['user_type'] == 'admin':
        return render_template('main.html', title='Main menu') 
    else:
        return render_template('customer_main.html', title='Main menu') 
    
@app.route('/users/manage', methods=['GET', 'POST'])
def manage_user():
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    u = user()
    action = request.args.get('action')
    pkval = request.args.get('pkval')

    if action == 'delete':  # Delete user
        u.deleteById(pkval)
        return render_template('ok_dialog.html', msg="User deleted successfully.")

    if action == 'insert':  # Add new user
        d = {
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'password2': request.form.get('password2'),
            'user_type': request.form.get('user_type'),
            'zipcode': request.form.get('zipcode'),
        }
        u.set(d)
        if u.verify_new():
            u.insert()
            return render_template('ok_dialog.html', msg="User added successfully.")
        return render_template('users/add.html', obj=u)

    if action == 'update':  # Update existing user
        u.getById(pkval)
        u.data[0]['email'] = request.form.get('email')
        u.data[0]['password'] = request.form.get('password')
        u.data[0]['password2'] = request.form.get('password2')
        u.data[0]['user_type'] = request.form.get('user_type')
        u.data[0]['zipcode'] = request.form.get('zipcode')

        if u.verify_update():
            u.update()
            return render_template('ok_dialog.html', msg="User updated successfully.")
        return render_template('users/manage.html', obj=u)

    if pkval is None:  # List all users
        u.getAll()
        return render_template('users_list.html', objs=u)

    if pkval == 'new':  # Add new user form
        u.createBlank()
        return render_template('users_add.html', obj=u)

    u.getById(pkval)  # Manage specific user
    return render_template('users_manage.html', obj=u)


@app.route('/pets/manage', methods=['GET', 'POST'])
def manage_pet():
    if not checkSession() or session['user']['user_type'] != 'admin':
        return redirect('/login')

    p = pet()
    action = request.args.get('action')
    pkval = request.args.get('pkval')

    if action == 'delete':  # Delete pet
        p.deleteById(pkval)
        return render_template('ok_dialog.html', msg="Pet deleted successfully.")

    if action == 'insert':  # Add new pet
        d = {
            'name': request.form.get('name'),
            'type': request.form.get('type'),
            'breed': request.form.get('breed'),
            'age': int(request.form.get('age')),
            'gender': request.form.get('gender'),
            'health_status': request.form.get('health_status'),
            'description': request.form.get('description'),
            'image_url': request.form.get('image_url'),
            'listing_date': request.form.get('listing_date'),
            'status': request.form.get('status'),
            'shelter_id': request.form.get('shelter_id'),
        }
        p.set(d)
        if p.verify_new():
            p.insert()
            return render_template('ok_dialog.html', msg="Pet added successfully.")
        return render_template('pets_add.html', obj=p)

    if action == 'update':  # Update existing pet
        p.getById(pkval)
        p.data[0]['name'] = request.form.get('name')
        p.data[0]['type'] = request.form.get('type')
        p.data[0]['breed'] = request.form.get('breed')
        p.data[0]['age'] = int(request.form.get('age'))
        p.data[0]['gender'] = request.form.get('gender')
        p.data[0]['health_status'] = request.form.get('health_status')
        p.data[0]['description'] = request.form.get('description')
        p.data[0]['image_url'] = request.form.get('image_url')
        p.data[0]['listing_date'] = request.form.get('listing_date')
        p.data[0]['status'] = request.form.get('status')
        p.data[0]['shelter_id'] = request.form.get('shelter_id')

        if p.verify_update():
            p.update()
            return render_template('ok_dialog.html', msg="Pet updated successfully.")
        return render_template('pets_manage.html', obj=p)

    if pkval is None:  # List all pets
        p.getAll()
        return render_template('pets_list.html', objs=p)

    if pkval == 'new':  # Add new pet form
        p.createBlank()
        return render_template('pets_add.html', obj=p)

    # Manage a specific pet
    p.getById(pkval)
    return render_template('pets_manage.html', obj=p)


@app.route('/pets/add', methods=['GET'])
def pets_add():
    return render_template('pets_add.html')


@app.route('/pets/edit/<int:pet_id>', methods=['GET'])
def pets_edit(pet_id):
    # Dummy data for frontend testing
    pet = {"pet_id": pet_id, "name": "Buddy", "type": "Dog", "breed": "Golden Retriever"}
    return render_template('pets_edit.html', pet=pet)




# @app.route('/users/manage',methods=['GET','POST'])
# def manage_user():
#     if checkSession() == False or session['user']['user_type'] != 'admin': 
#         return redirect('/login')
#     o = user()
#     action = request.args.get('action')
#     pkval = request.args.get('pkval')
#     if action is not None and action == 'delete': #action=delete&pkval=123
#         o.deleteById(request.args.get('pkval'))
#         return render_template('ok_dialog.html',msg= "Deleted.")
#     if action is not None and action == 'insert':
#         d = {}
#         d['name'] = request.form.get('name')
#         d['role'] = request.form.get('role')
#         d['password'] = request.form.get('password')
#         d['password2'] = request.form.get('password2')
#         o.set(d)
#         if o.verify_new():
#             o.insert()
#             uid = o.data[0][o.pk]
#             return render_template('ok_dialog.html',msg= f"User uid={uid} added.")
#         else:
#             return render_template('users/add.html',obj = o)
#     if action is not None and action == 'update':
#         o.getById(pkval)
#         o.data[0]['name'] = request.form.get('name')
#         o.data[0]['role'] = request.form.get('role')
#         o.data[0]['password'] = request.form.get('password')
#         o.data[0]['password2'] = request.form.get('password2')
#         if o.verify_update():
#             o.update()
#             return render_template('ok_dialog.html',msg= "User updated. <")
#         else:
#             return render_template('users/manage.html',obj = o)
        
#     if pkval is None: #list all items
#         o.getAll()
#         return render_template('users/list.html',objs = o)
#     if pkval == 'new':
#         o.createBlank()
#         return render_template('users/add.html',obj = o)
#     else:
#         print(pkval)
#         o.getById(pkval)
#         return render_template('users/manage.html',obj = o)

@app.route('/vehicles/manage',methods=['GET','POST'])
def manage_vehicles():
    if checkSession() == False or session['user']['role'] != 'admin': 
        return redirect('/login')
    o = vehicle()
    action = request.args.get('action')
    pkval = request.args.get('pkval')
    u = user()
    u.getAll()
    o.owners = u
    if action is not None and action == 'delete': #action=delete&pkval=123
        o.deleteById(request.args.get('pkval'))
        return render_template('ok_dialog.html',msg= "Deleted.")
    if action is not None and action == 'insert':
        d = {}
        d['make'] = request.form.get('make')
        d['model'] = request.form.get('model')
        d['year'] = request.form.get('year')
        d['uid'] = request.form.get('uid')
        d['owner_uid'] = request.form.get('owner_uid')#session['user']['uid']
        d['created_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        o.set(d)
        if o.verify_new():
            o.insert()
            return render_template('ok_dialog.html',msg= "Vehicle added.")
        else:
            return render_template('vehicles/add.html',obj = o)
    if action is not None and action == 'update':
        o.getById(pkval)
        o.data[0]['make'] = request.form.get('make')
        o.data[0]['model'] = request.form.get('model')
        o.data[0]['uid'] = request.form.get('uid')
        o.data[0]['year'] = request.form.get('year')
        o.data[0]['owner_uid'] = request.form.get('owner_uid')
        if o.verify_update():
            o.update()
            return render_template('ok_dialog.html',msg= "Vehicle updated.")
        else:
            return render_template('vehicles/manage.html',obj = o)
        
    if pkval is None: #list all items
        o.getAll()
        return render_template('vehicles/list.html',objs = o)
    if pkval == 'new':
        o.createBlank()
        return render_template('vehicles/add.html',obj = o)
    else:
        print(pkval)
        o.getById(pkval)
        return render_template('vehicles/manage.html',obj = o)



# endpoint route for static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

#standalone function to be called when we need to check if a user is logged in.
def checkSession():
    if 'active' in session.keys():
        timeSinceAct = time.time() - session['active']
        print(timeSinceAct)
        if timeSinceAct > 500:
            session['msg'] = 'Your session has timed out.'
            return False
        else:
            session['active'] = time.time()
            return True
    else:
        return False      
  
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug=True)   