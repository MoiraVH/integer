from db_con import db
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Conexión a la colección de usuarios en MongoDB
user_collection = db['encargados']
caseta_collection = db['casetas']
# encargados_collection = db['encargados']



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
            })

        except Exception as e:
            raise Exception(f"Error al guardar el usuario en MongoDB: {e}")
    
    @staticmethod
    def update_user(self):
        """Actualiza el usuario en MongoDB."""
        


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

class Casetas:
    def __init__(self, numCaseta, ubicacion, estado, encargado, celCaseta, controlE):
        self.numCaseta = numCaseta
        self.ubicacion = ubicacion
        self.estado = estado
        self.encargado = encargado
        self.celCaseta = celCaseta
        self.controlE = controlE

    def save(self):
        """Guarda la caseta en MongoDB."""
        try:
            if caseta_collection.find_one({"numCaseta": self.numCaseta}):
                raise ValidationError("La caseta ya está registrada.")
            caseta_collection.insert_one({
                "numCaseta": self.numCaseta,
                "ubicacion": self.ubicacion,
                "estado": self.estado,
                "encargado": self.encargado,
                "celCaseta": self.celCaseta,
                "controlE": self.controlE
                }) 
            
        except Exception as e:
            raise Exception(f"Error al guardar la caseta en MongoDB: {e}")

    