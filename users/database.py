from users import config, log
from pymongo import MongoClient

def get_db():
    return MongoClient(config.DATABASE).users.users
