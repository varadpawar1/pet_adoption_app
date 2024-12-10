from models.baseObject import baseObject

class pet(baseObject):
    def __init__(self):
        self.setup()  # Initialize connection, fields, and primary key
        self.valid_status = ['Available', 'Adopted', 'Pending']  # Example statuses for pets

    def verify_new(self, n=0):
        """Validate data for creating a new pet."""
        self.errors = []

        # Validate name
        if not self.data[n].get('name'):
            self.errors.append('Name cannot be blank.')

        # Validate type
        if not self.data[n].get('type'):
            self.errors.append('Type cannot be blank.')

        # Validate breed
        if not self.data[n].get('breed'):
            self.errors.append('Breed cannot be blank.')

        # Validate age
        try:
            age = int(self.data[n]['age'])
            if age < 0:
                self.errors.append('Age must be a non-negative integer.')
        except (ValueError, TypeError):
            self.errors.append('Age must be a valid integer.')

        # Validate gender
        if self.data[n]['gender'] not in ['Male', 'Female', 'Other']:
            self.errors.append("Gender must be 'Male', 'Female', or 'Other'.")

        # Validate health_status
        if not self.data[n].get('health_status'):
            self.errors.append('Health status cannot be blank.')

        # Validate status
        if self.data[n]['status'] not in self.valid_status:
            self.errors.append(f"Status must be one of {self.valid_status}.")

        # Validate shelter_id
        try:
            shelter_id = int(self.data[n]['shelter_id'])
            if shelter_id <= 0:
                self.errors.append('Shelter ID must be a positive integer.')
        except (ValueError, TypeError):
            self.errors.append('Shelter ID must be a valid integer.')

        # Optional fields: description, image_url
        if 'description' in self.data[n] and len(self.data[n]['description']) > 500:
            self.errors.append('Description cannot exceed 500 characters.')

        if 'image_url' in self.data[n] and not self.data[n]['image_url'].startswith(('http://', 'https://')):
            self.errors.append('Image URL must start with "http://" or "https://".')

        return len(self.errors) == 0

    def verify_update(self, n=0):
        """Validate data for updating an existing pet."""
        self.errors = []

        # Validate only the fields being updated
        updatable_fields = ['name', 'type', 'breed', 'age', 'gender', 'health_status', 
                            'description', 'image_url', 'status', 'shelter_id']
        for field in updatable_fields:
            if field in self.data[n]:
                if field == 'age':
                    try:
                        age = int(self.data[n]['age'])
                        if age < 0:
                            self.errors.append('Age must be a non-negative integer.')
                    except (ValueError, TypeError):
                        self.errors.append('Age must be a valid integer.')
                elif field == 'gender' and self.data[n][field] not in ['Male', 'Female', 'Other']:
                    self.errors.append("Gender must be 'Male', 'Female', or 'Other'.")
                elif field == 'status' and self.data[n][field] not in self.valid_status:
                    self.errors.append(f"Status must be one of {self.valid_status}.")
                elif field == 'shelter_id':
                    try:
                        shelter_id = int(self.data[n]['shelter_id'])
                        if shelter_id <= 0:
                            self.errors.append('Shelter ID must be a positive integer.')
                    except (ValueError, TypeError):
                        self.errors.append('Shelter ID must be a valid integer.')
                elif field == 'description' and len(self.data[n][field]) > 500:
                    self.errors.append('Description cannot exceed 500 characters.')
                elif field == 'image_url' and not self.data[n][field].startswith(('http://', 'https://')):
                    self.errors.append('Image URL must start with "http://" or "https://".')

        return len(self.errors) == 0
