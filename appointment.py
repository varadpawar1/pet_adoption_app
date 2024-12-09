from baseObject import baseObject
from datetime import datetime

class appointment(baseObject):
    def __init__(self):
        self.setup()  # Initialize connection, fields, and primary key
        self.valid_status = ['Scheduled', 'Completed', 'Cancelled']  # Example statuses for appointments

    def verify_new(self, n=0):
        """Validate data for creating a new appointment."""
        self.errors = []

        # Validate appointment_date
        if not self.data[n].get('appointment_date'):
            self.errors.append('Appointment date cannot be blank.')
        else:
            try:
                datetime.strptime(self.data[n]['appointment_date'], '%Y-%m-%d')
            except ValueError:
                self.errors.append('Appointment date must be in YYYY-MM-DD format.')

        # Validate status
        if self.data[n].get('status') not in self.valid_status:
            self.errors.append(f"Status must be one of {self.valid_status}.")

        # Validate shelter_id
        try:
            shelter_id = int(self.data[n]['shelter_id'])
            if shelter_id <= 0:
                self.errors.append('Shelter ID must be a positive integer.')
        except (ValueError, TypeError):
            self.errors.append('Shelter ID must be a valid integer.')

        # Validate user_id
        try:
            user_id = int(self.data[n]['user_id'])
            if user_id <= 0:
                self.errors.append('User ID must be a positive integer.')
        except (ValueError, TypeError):
            self.errors.append('User ID must be a valid integer.')

        return len(self.errors) == 0

    def verify_update(self, n=0):
        """Validate data for updating an existing appointment."""
        self.errors = []

        # Validate only the fields being updated
        updatable_fields = ['appointment_date', 'status', 'shelter_id', 'user_id']
        for field in updatable_fields:
            if field in self.data[n]:
                if field == 'appointment_date':
                    try:
                        datetime.strptime(self.data[n][field], '%Y-%m-%d')
                    except ValueError:
                        self.errors.append('Appointment date must be in YYYY-MM-DD format.')
                elif field == 'status' and self.data[n][field] not in self.valid_status:
                    self.errors.append(f"Status must be one of {self.valid_status}.")
                elif field in ['shelter_id', 'user_id']:
                    try:
                        id_value = int(self.data[n][field])
                        if id_value <= 0:
                            self.errors.append(f"{field.replace('_', ' ').title()} must be a positive integer.")
                    except (ValueError, TypeError):
                        self.errors.append(f"{field.replace('_', ' ').title()} must be a valid integer.")

        return len(self.errors) == 0
