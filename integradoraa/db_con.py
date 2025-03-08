import pymongo

url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['login_db']
collection = db['users']

# Check MongoDB connection
try:
    client.admin.command('ping')
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"Could not connect to MongoDB: {e}")


