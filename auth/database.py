from pymongo import MongoClient

from auth import log, config

def get_db():
    return MongoClient(config.DATABASE).users.users
