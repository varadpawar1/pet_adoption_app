from baseObject import baseObject
from datetime import datetime

class adoption(baseObject):
    def __init__(self):
        self.setup()  # Initialize connection, fields, and primary key
        self.valid_status = ['Pending', 'Approved', 'Rejected']  # Example statuses for adoptions

    def verify_new(self, n=0):
        """Validate data for creating a new adoption."""
        self.errors = []

        # Validate request_date
        if not self.data[n].get('request_date'):
            self.errors.append('Request date cannot be blank.')
        else:
            request_date = self.data[n]['request_date']
            if not isinstance(request_date, str):  # Ensure it's a string
                request_date = request_date.strftime('%Y-%m-%d')
            try:
                datetime.strptime(request_date, '%Y-%m-%d')
            except ValueError:
                self.errors.append('Request date must be in YYYY-MM-DD format.')

        # Validate status
        if self.data[n].get('status') not in self.valid_status:
            self.errors.append(f"Status must be one of {self.valid_status}.")

        # Validate adoption_date
        if self.data[n].get('adoption_date'):
            adoption_date = self.data[n]['adoption_date']
            if not isinstance(adoption_date, str):  # Ensure it's a string
                adoption_date = adoption_date.strftime('%Y-%m-%d')
            try:
                datetime.strptime(adoption_date, '%Y-%m-%d')
            except ValueError:
                self.errors.append('Adoption date must be in YYYY-MM-DD format.')

        # Validate user_id
        try:
            user_id = int(self.data[n]['user_id'])
            if user_id <= 0:
                self.errors.append('User ID must be a positive integer.')
        except (ValueError, TypeError):
            self.errors.append('User ID must be a valid integer.')

        # Validate pet_id
        try:
            pet_id = int(self.data[n]['pet_id'])
            if pet_id <= 0:
                self.errors.append('Pet ID must be a positive integer.')
        except (ValueError, TypeError):
            self.errors.append('Pet ID must be a valid integer.')

        return len(self.errors) == 0

    def verify_update(self, n=0):
        """Validate data for updating an existing adoption."""
        self.errors = []

        # Validate only the fields being updated
        updatable_fields = ['request_date', 'status', 'adoption_date', 'user_id', 'pet_id']
        for field in updatable_fields:
            if field in self.data[n]:
                if field == 'request_date':
                    request_date = self.data[n][field]
                    if not isinstance(request_date, str):  # Ensure it's a string
                        request_date = request_date.strftime('%Y-%m-%d')
                    try:
                        datetime.strptime(request_date, '%Y-%m-%d')
                    except ValueError:
                        self.errors.append('Request date must be in YYYY-MM-DD format.')
                elif field == 'adoption_date':
                    adoption_date = self.data[n][field]
                    if not isinstance(adoption_date, str):  # Ensure it's a string
                        adoption_date = adoption_date.strftime('%Y-%m-%d')
                    try:
                        datetime.strptime(adoption_date, '%Y-%m-%d')
                    except ValueError:
                        self.errors.append('Adoption date must be in YYYY-MM-DD format.')
                elif field == 'status' and self.data[n][field] not in self.valid_status:
                    self.errors.append(f"Status must be one of {self.valid_status}.")
                elif field in ['user_id', 'pet_id']:
                    try:
                        id_value = int(self.data[n][field])
                        if id_value <= 0:
                            self.errors.append(f"{field.replace('_', ' ').title()} must be a positive integer.")
                    except (ValueError, TypeError):
                        self.errors.append(f"{field.replace('_', ' ').title()} must be a valid integer.")

        return len(self.errors) == 0
