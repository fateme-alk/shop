from exceptions import PhoneNumberValueError, EmailValueError
from validators import validate_phone, validate_email

class Person:

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self._phone = None
        self._email = None
    
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, num):
        if validate_phone(num):
            self._phone = num
        else:
            raise PhoneNumberValueError
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if validate_email(email):
            self._email = email
        else:
            raise EmailValueError

