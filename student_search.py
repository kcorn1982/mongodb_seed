import pymongo

conn_str = "mongodb://root:password@localhost:27017"

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

student_db = client["students"]
student_collection = student_db["student_data"]


def find_one():
    print(student_collection.find_one())


def find_all():
    for student in student_collection.find():
        print(student)


def query(query_syntax):
    for student_found in student_collection.find(query_syntax):
        print(student_found)



    # query({"graduation_year": {"$gt": "2018"}})
