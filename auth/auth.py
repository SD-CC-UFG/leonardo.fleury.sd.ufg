import jwt
import logging
import yaml
import json

from datetime import datetime, timedelta

from nameko.rpc import rpc
from bson.json_util import dumps
from bcrypt import hashpw, gensalt

from auth.config import config
from auth.database import get_db

log = logging.getLogger(__name__)

class Auth(object):
    name = "auth"

    @rpc
    def login(self, username, password):
        mongo = get_db()

        user = mongo.find_one({'_id': username})

        if user:
            if (hashpw(password.encode('utf-8'), user['password']) == user['password']):
                log.info("User was authenticate.")
                return json.dumps({
                    "code": 0
                })
            else:
                log.info("Incorrect password.")
                return json.dumps({
                    "code": 1,
                    "error": "Incorrect password."
                })
        else:
            log.info("Could not find user.")
            return json.dumps({
                    "code": 1,
                    "error": "Could not find user."
                })