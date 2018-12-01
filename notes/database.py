from pymongo import MongoClient


def get_db():
    return MongoClient("mongodb+srv://notes_admin:GhUTriaIlUzOVmIC@notesdb-ytix1.gcp.mongodb.net/notes?retryWrites=true").db.notes
