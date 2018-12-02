from pymongo import MongoClient

def get_db():
    return MongoClient("mongodb+srv://users_admin:sHM3oaMqcM8PaTML@notesdb-ytix1.gcp.mongodb.net/notes?retryWrites=true").users.users
