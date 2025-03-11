from django.db import models
from db_con import db
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from secrets import token_urlsafe
from django.core.validators import validate_email

user_collection = db['users']
class UserModel:
    def __init__(self, name, email, lastname, location, phone, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.location = location
        self.phone = phone
        self.password = make_password(password)

    def save(self):
        """Guarda el usuario en MongoDB."""
        try:
            validate_email(self.email)  # Validar formato de email
        except ValidationError:
            raise ValidationError("El email no tiene un formato válido.")

        try:
            user_collection.insert_one({
                "name": self.name,
                "lastname": self.lastname,
                "location": self.location,
                "phone": self.phone, 
                "email": self.email,
                "password": self.password
            })
        except Exception as e:
            raise Exception(f"Error al guardar el usuario en MongoDB: {e}")

    @staticmethod
    def get_user_by_email(email):
        """Busca un usuario por email."""
        return user_collection.find_one({"email": email})

    @staticmethod
    def check_credentials(email, password):
        """Verifica si las credenciales son correctas."""
        user = UserModel.get_user_by_email(email)
        if user and check_password(password, user["password"]):
            return user
        return None