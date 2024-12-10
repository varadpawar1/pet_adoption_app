from models.user import user
from models.baseObject import baseObject
from models.shelter import shelter
from models.adoption import adoption
# u = user()
# u.truncate()
# u.set({
#     'email': 'john@example.com',
#     'password': '123',            # Plain text password (to be hashed)
#     'password2': '123',           # Confirm password
#     'phone_number': '1234567832',
#     'registration_date': '2024-11-19',  # Use a valid date format
#     'Address': '123 Main St',
#     'zipcode': '13676',
#     'name': 'John Cena',
#     'user_type': 'customer',         # 'admin' or 'customer'
#     'shelter_id': 2               # Valid shelter ID (foreign key)
# })
# if u.verify_new():
#     u.insert()
# else:
#     print(u.errors)



# u = user()
# u.getById(4)
# print(u.data)
# u.data[0]['user_type'] = 'customer'
# if u.verify_update():
#     u.update()
#     #print(u.data[0][u.pk])
# else:
#     print(u.errors)

# u = user()
# u.getById(5)
# print(u.data)


# u = user()
# u.getById(6)
# print(u.data)

# s = shelter()
# s.set({
#     'shelter_name': 'Happy Paws Shelter',
#     'address': '123 Main St, Springfield',
#     'contact': '555-123-4567',
#     'website_url': 'https://happypawshelter.org'
# })
# if s.verify_new():
#     s.insert()
#     print("Shelter added successfully.")
# else:
#     print("Errors:", s.errors)

# s = shelter()
# s.getById(1)  # Assuming shelter_id = 1
# s.data[0]['address'] = '456 Elm St, Springfield'
# s.data[0]['website_url'] = 'http://newwebsite.org'
# s.data[0]['shelter_name'] = 'Happy soul shelter'
# if s.verify_update():
#     s.update()
#     print("Shelter updated successfully.")
# else:
#     print("Errors:", s.errors)

# a = adoption()
# a.set({
#     'request_date': '2024-11-19',
#     'status': 'Pending',
#     'adoption_date': None,
#     'user_id': 8,
#     'pet_id': 2
# })
# if a.verify_new():
#     a.insert()
#     print("Adoption record added successfully.")
# else:
#     print("Errors:", a.errors)

a = adoption()
a.getById(1)  # Assuming adoption_id = 1
a.data[0]['status'] = 'Approved'
a.data[0]['adoption_date'] = '2024-11-15'
if a.verify_update():
    a.update()
    print("Adoption record updated successfully.")
else:
    print("Errors:", a.errors)
