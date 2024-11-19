from user import user
from baseObject import baseObject

u = user()
u.truncate()
u.set({'name':'conlontj','password':'134','password2':'134','role':'admin'})
if u.verify_new():
    u.insert()
else:
    print(u.errors)



u = user()
u.getById(1)
u.data[0]['role'] = 'employee'
if u.verify_update():
    u.update()
    #print(u.data[0][u.pk])
else:
    print(u.errors)

u = user()
u.getById(0)
print(u.data)


u = user()
u.getById(1)
print(u.data)