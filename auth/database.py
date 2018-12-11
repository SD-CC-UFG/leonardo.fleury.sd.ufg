import logging
from pymongo import MongoClient

from auth.config import config

log = logging.getLogger(__name__)

def get_db():
    try:
        log.debug('Connecting to database...')
        db = MongoClient(config['DATABASE']).users.users
        log.debug('Connected.')
        return db
    except:
        log.debug('Error while connecting to database.')
        return None

