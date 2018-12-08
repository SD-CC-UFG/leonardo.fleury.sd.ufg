from pymongo import MongoClient
from notes import log, config

def get_db(user=None):
    return MongoClient(config.DATABASE).notes.notes
