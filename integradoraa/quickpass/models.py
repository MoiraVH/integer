from django.conf import settings
import hashlib
import os

db = settings.MONGO_USERS

class User:
    def __init__(self, name, lastname, email, location, phone, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.residencia = location
        self.number = phone
        self.salt = os.urandom(32).hex()  # Crear un salt único
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        """Hash la contraseña con salt"""
        return hashlib.sha256((password + self.salt).encode()).hexdigest()

    def save(self):
        """Guardar usuario en MongoDB"""
        db.insert_one(self.__dict__)

    @staticmethod
    def get_by_email(email):
        """Buscar usuario por email"""
        return db.find_one({"email": email})

    @staticmethod
    def verify_password(email, password):
        """Verificar contraseña"""
        user = User.get_by_email(email)
        if not user:
            return False
        hashed = hashlib.sha256((password + user["salt"]).encode()).hexdigest()
        return hashed == user["password"]