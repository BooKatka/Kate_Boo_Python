class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_user_info(self):
        return f"User's name: {self.name}, last_name: {self.surname}"
    