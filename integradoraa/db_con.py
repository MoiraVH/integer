import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['quickpass_db']
collection = db['users']
