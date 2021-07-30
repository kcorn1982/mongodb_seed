import pymongo
import json

conn_str = "mongodb://root:password@localhost:27017"

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

student_db = client["students"]

student_collection = student_db["student_data"]

with open("test_user_data.json") as user_data:
    student_collection.insert_many(json.load(user_data))
