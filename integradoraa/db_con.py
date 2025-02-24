from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # Conexión a MongoDB
db = client["login_db"]  # Nombre de la base de datos

