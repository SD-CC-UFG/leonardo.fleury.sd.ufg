from pymongo import MongoClient


def get_db(user=None):
    if user:
        return MongoClient("mongodb+srv://notes_admin:GhUTriaIlUzOVmIC@notesdb-ytix1.gcp.mongodb.net/notes?retryWrites=true").notes[user]
    else:
        raise Exception("User was not set.")

