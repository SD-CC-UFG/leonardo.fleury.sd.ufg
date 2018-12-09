import logging

from pymongo import MongoClient
from notes.config import config

log = logging.getLogger(__name__)

def get_db(user=None):
    return MongoClient(config['DATABASE']).notes.notes
