import hashlib
from models.baseObject import baseObject

class user(baseObject):
    def __init__(self):
        self.setup()
        self.user_type = [
            {'value': 'admin', 'text': 'Administrator'},
            {'value': 'customer', 'text': 'Customer'}
        ]
    
    def hashPassword(self, pw):
        pw = pw + 'xyz'
        return hashlib.md5(pw.encode('utf-8')).hexdigest()
    
    def verify_new(self, n=0):
        self.errors = []
        if self.data[n]['email'] == '':
            self.errors.append('Email cannot be blank.')
        else:
            u = user()
            u.getByField('email', self.data[n]['email'])
            if len(u.data) > 0:
                self.errors.append('Email already in use.')

        if self.data[n]['password'] != self.data[n]['password2']:
            self.errors.append('Retyped password must match.')
        
        if len(self.data[n]['password']) < 3:
            self.errors.append('Password needs to be more than 3 characters.')
        else:
            self.data[n]['password'] = self.hashPassword(self.data[n]['password'])
        
        # Check shelter_id for admin users
        if self.data[n]['user_type'] == 'admin' and not self.data[n].get('shelter_id'):
            self.errors.append('Shelter ID is required for admin users.')

        # Ensure shelter_id is null for non-admin users
        if self.data[n]['user_type'] != 'admin':
            self.data[n]['shelter_id'] = None
        
        rl = [user_type['value'] for user_type in self.user_type]
        if self.data[n]['user_type'] not in rl:
            self.errors.append(f'User type must be one of {rl}.')
        
        if self.data[n]['zipcode'] == '':
            self.errors.append('Zipcode cannot be blank.')

        if len(self.errors) > 0:
            return False
        return True
    
    def verify_update(self, n=0):
        self.errors = []

        if self.data[n]['email'] == '':
            self.errors.append('Email cannot be blank.')
        else:
            u = user()
            u.getByField('email', self.data[n]['email'])
            if len(u.data) > 0 and u.data[0][u.pk] != self.data[n][self.pk]:
                self.errors.append('Email already in use.')
        
        if 'password2' in self.data[n].keys():  # User intends to change password
            if self.data[n]['password'] != self.data[n]['password2']:
                self.errors.append('Retyped password must match.')
            if len(self.data[n]['password']) < 3:
                self.errors.append('Password must be more than 3 characters.')
            else:
                self.data[n]['password'] = self.hashPassword(self.data[n]['password'])
        else:
            del self.data[n]['password']  # Password unchanged
        
        rl = [user_type['value'] for user_type in self.user_type]
        if self.data[n]['user_type'] not in rl:
            self.errors.append(f'User type must be one of {rl}.')

        if len(self.errors) > 0:
            return False
        return True

    def tryLogin(self, email, password):
        pwd = self.hashPassword(password)
        sql = f"SELECT * FROM `{self.tn}` WHERE `email` = %s AND `password` = %s;"
        self.cur.execute(sql, (email, pwd))
        self.data = [row for row in self.cur]
        return len(self.data) == 1

        