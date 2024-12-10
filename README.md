
# 🐾 **Pet Adoption Management System**

This project is a web application designed to facilitate pet adoptions and shelter management. It allows administrators to manage users, shelters, pets, adoptions, and appointments, while customers can browse pets, book appointments, and request adoptions.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Database Schema](#database-schema)
5. [Folder Structure](#folder-structure)
6. [Key Functionalities](#key-functionalities)
7. [Screenshots](#screenshots)
8. [License](#license)

---

## Features

### For **Customers**
- View available shelters and pets.
- Book appointments to visit shelters.
- Request pet adoptions.
- View the status of their appointment or adoption request.
- Secure user authentication and session management.

### For **Admins**
- Manage users (add, update, delete).
- Manage shelters (add, update, delete).
- Manage pets (add, update, delete).
- Manage adoptions and appointments.
- Secure access to admin options.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy (MySQL)
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja2
- **Image Handling**: Static files for pet and shelter images
- **Deployment**: Flask development server

---

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pet-adoption-system.git
   cd pet-adoption-system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   - Update `SQLALCHEMY_DATABASE_URI` in `app.py` with your MySQL credentials:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
     ```
   - Initialize the database:
     ```bash
     flask db init
     flask db migrate -m "Initial migration."
     flask db upgrade
     ```

6. **Run the Flask app**:
   ```bash
   flask run
   ```
   The app should be accessible at `http://127.0.0.1:5000`.

---

## Database Schema

### Shelters Table
```sql
CREATE TABLE shelters (
    shelter_id INT AUTO_INCREMENT PRIMARY KEY,
    shelter_name VARCHAR(100),
    address VARCHAR(255),
    contact VARCHAR(50),
    website_url VARCHAR(255)
);
```

### Pets Table
```sql
CREATE TABLE pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(50),
    breed VARCHAR(100),
    age INT,
    health_status VARCHAR(100),
    shelter_id INT,
    adoption_requested BOOLEAN DEFAULT FALSE,
    appointment_booked BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (shelter_id) REFERENCES shelters(shelter_id)
);
```

### Users Table
```sql
CREATE TABLE users (
    uid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(50)
);
```

---

## Folder Structure

```
pet-adoption-system/
│
├── static/
│   ├── Pets/
│   │   ├── dog1.png
│   │   ├── cat1.png
│   │   └── ...
│   └── css/
│       └── styles.css
│
├── templates/
│   ├── base.html
│   ├── customer_main.html
│   ├── manage_user.html
│   └── ...
│
├── app.py
├── models.py
├── requirements.txt
└── README.md
```

---

## Key Functionalities

### 1. **Customer Main Menu**
   - Displays shelters and pets.
   - Allows customers to:
     - Book appointments.
     - Request adoptions.
   - Template: `customer_main.html`

### 2. **Admin User Management**
   - Add, update, and delete users.
   - Form includes fields for name, password, role.
   - Template: `manage_user.html`

### 3. **Navigation Protection**
   - Prevent back navigation after logout using JavaScript:
     ```html
     <script>
         history.pushState(null, document.title, location.href);
         window.addEventListener('popstate', function () {
             history.pushState(null, document.title, location.href);
         });
     </script>
     ```

### 4. **Pet Images**
   - Pet images are stored in the `static/Pets/` folder and displayed dynamically using:
     ```html
     <img src="{{ url_for('static', filename='Pets/' ~ pet.name ~ '.png') }}" alt="{{ pet.name }}">
     ```

---

## Screenshots

### **Customer Main Menu**
![Customer Main Menu](static/screenshots/customer_main.png)

### **Manage Users Form**
![Manage Users Form](static/screenshots/manage_user.png)

---


### 🚀 **Happy Coding!** 🐶🐱

