from django.db import models
from db_con import db
from django.contrib.auth.hashers import make_password, check_password

user_collection = db['users']
class UserModel:
    def __init__(self, name, email, lastname, location, phone, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.location = location
        self.phone = phone
        self.password = make_password(password)  # Hashea la contraseña antes de guardarla

    def save(self):
        """Guarda el usuario en MongoDB."""
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
            print(f"Error al guardar el usuario en MongoDB: {e}")


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
