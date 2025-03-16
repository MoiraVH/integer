from db_con import db
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Conexión a la colección de usuarios en MongoDB
user_collection = db['users']

# Definir los roles permitidos
VALID_ROLES = {"user", "worker", "admin"}

class UserModel:
    def __init__(self, name, email, lastname, location, phone, password, role="user"):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.location = location
        self.phone = phone
        self.password = make_password(password)

    def save(self):
        """Guarda el usuario en MongoDB."""
        try:
            validate_email(self.email)  # Validar email
            if user_collection.find_one({"email": self.email}):
                raise ValidationError("El correo ya está registrado.")

            user_collection.insert_one({
                "name": self.name,
                "lastname": self.lastname,
                "location": self.location,
                "phone": self.phone,
                "email": self.email,
                "password": self.password,
                # "role": self.role  # Guardamos el rol
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

    # @staticmethod
    # def get_role(email):
    #     """Obtiene el rol de un usuario por su email."""
    #     user = UserModel.get_user_by_email(email)
    #     return user["role"] if user else None
    

