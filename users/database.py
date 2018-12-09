import logging

from users.config import config
from pymongo import MongoClient

log = logging.getLogger(__name__)

def get_db():
    return MongoClient(config['DATABASE']).users.users
