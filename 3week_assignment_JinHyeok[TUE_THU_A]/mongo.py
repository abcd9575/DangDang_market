from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.local

collection = db.startup_log

row = collection.find_one()
print(row)