import logging
from pymongo import MongoClient

from auth.config import config

log = logging.getLogger(__name__)

def get_db():
    return MongoClient(config['DATABASE']).users.users
