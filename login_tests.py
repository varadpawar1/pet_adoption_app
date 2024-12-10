from models.user import user
from models.baseObject import baseObject
from models.pet import pet

u = user()
p = pet()
u.truncate()
# u.set({
#     'email': 'bhanu@example.com',
#     'password': '123',            # Plain text password (to be hashed)
#     'password2': '123',           # Confirm password
#     'phone_number': '1234567832',
#     'registration_date': '2024-11-18',  # Use a valid date format
#     'Address': '123 Main St',
#     'zipcode': '13676',
#     'name': 'Bhanu P',
#     'user_type': 'customer',         # 'admin' or 'customer'
#     'shelter_id': 2               # Valid shelter ID (foreign key)
# })

p.set({
    'name': 'Buddy',                    # Name of the pet
    'type': 'Dog',                      # Type of the pet (e.g., Dog, Cat)
    'breed': 'Golden Retriever',        # Breed
    'age': 3,                           # Age in years
    'gender': 'Male',                   # Gender (Male, Female, Other)
    'health_status': 'Healthy',         # Health status (e.g., Healthy, Needs medication)
    'description': 'A friendly and active dog looking for a home.',  # Description
    'image_url': 'https://potsdamhumanesociety.org/wp-content/uploads/2023/11/margaery.jpg', # URL of the pet's image
    'listing_date': '2024-11-18',       # Date the pet was listed
    'status': 'Available',              # Status (Available, Adopted, Pending)
    'shelter_id': 1                     # Shelter ID (foreign key)
})

if p.verify_new():
    p.insert()
else:
    print(p.errors)

# u = user()
# if u.tryLogin("pawarv@example.com","134"):
#     print("Login ok.")
# else:
#     print("Login failed.")