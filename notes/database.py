import logging

from pymongo import MongoClient
from notes.config import config

log = logging.getLogger(__name__)

def get_db(user=None):
    try:
        db = MongoClient(config['DATABASE']).notes.notes
    except:
        log.debug('Could not connect to database')
