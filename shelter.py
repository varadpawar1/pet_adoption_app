from baseObject import baseObject

class shelter(baseObject):
    def __init__(self):
        self.setup()  # Initialize connection, fields, and primary key
        self.valid_url_prefixes = ['http://', 'https://']  # Valid URL prefixes for website URLs

    def verify_new(self, n=0):
        """Validate data for creating a new shelter."""
        self.errors = []

        # Validate shelter_name
        if not self.data[n].get('shelter_name') or self.data[n]['shelter_name'].strip() == '':
            self.errors.append('Shelter name cannot be blank.')

        # Validate address
        if not self.data[n].get('address') or self.data[n]['address'].strip() == '':
            self.errors.append('Address cannot be blank.')

        # Validate contact
        if not self.data[n].get('contact') or self.data[n]['contact'].strip() == '':
            self.errors.append('Contact cannot be blank.')

        # Validate website_url
        if 'website_url' in self.data[n]:
            website_url = self.data[n]['website_url']
            if website_url and not any(website_url.startswith(prefix) for prefix in self.valid_url_prefixes):
                self.errors.append('Website URL must start with "http://" or "https://".')

        return len(self.errors) == 0

    def verify_update(self, n=0):
        """Validate data for updating an existing shelter."""
        self.errors = []

        # Validate only the fields being updated
        updatable_fields = ['shelter_name', 'address', 'contact', 'website_url']
        for field in updatable_fields:
            if field in self.data[n]:
                if field == 'shelter_name' and (not self.data[n][field] or self.data[n][field].strip() == ''):
                    self.errors.append('Shelter name cannot be blank.')
                elif field == 'address' and (not self.data[n][field] or self.data[n][field].strip() == ''):
                    self.errors.append('Address cannot be blank.')
                elif field == 'contact' and (not self.data[n][field] or self.data[n][field].strip() == ''):
                    self.errors.append('Contact cannot be blank.')
                elif field == 'website_url':
                    website_url = self.data[n][field]
                    if website_url and not any(website_url.startswith(prefix) for prefix in self.valid_url_prefixes):
                        self.errors.append('Website URL must start with "http://" or "https://".')

        return len(self.errors) == 0
