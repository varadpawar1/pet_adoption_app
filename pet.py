from baseObject import baseObject

class pet(baseObject):
    def __init__(self):
        self.setup()  # Initialize connection, fields, and primary key
        self.valid_status = ['Available', 'Adopted', 'Pending']  # Example statuses for pets

    def verify_new(self, n=0):
        """Validate data for creating a new pet."""
        self.errors = []

        # Validate name
        if self.data[n]['name'] == '':
            self.errors.append('Name cannot be blank.')

        # Validate type
        if self.data[n]['type'] == '':
            self.errors.append('Type cannot be blank.')

        # Validate breed
        if self.data[n]['breed'] == '':
            self.errors.append('Breed cannot be blank.')

        # Validate age
        if not isinstance(self.data[n]['age'], int) or self.data[n]['age'] < 0:
            self.errors.append('Age must be a non-negative integer.')

        # Validate gender
        if self.data[n]['gender'] not in ['Male', 'Female', 'Other']:
            self.errors.append("Gender must be 'Male', 'Female', or 'Other'.")

        # Validate status
        if self.data[n]['status'] not in self.valid_status:
            self.errors.append(f"Status must be one of {self.valid_status}.")

        # Validate shelter_id
        if self.data[n]['shelter_id'] is None or self.data[n]['shelter_id'] == '':
            self.errors.append('Shelter ID cannot be blank.')

        return len(self.errors) == 0

    def verify_update(self, n=0):
        """Validate data for updating an existing pet."""
        self.errors = []

        # Reuse verification logic for new pets
        return self.verify_new(n)
