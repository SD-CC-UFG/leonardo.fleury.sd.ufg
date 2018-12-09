import jwt
import logging
import yaml

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
                token = self.__encode_auth_token(username)
                log.info("User was authenticate.")
                return dumps(token)
            else:
                log.info("User was not authenticate.")
                return 1
        else:
            log.info("User was not authenticate.")
            return 1

    def __encode_auth_token(self, username):
        try:
            payload = {
                'iss': 'notes auth server',
                'exp': datetime.utcnow() + timedelta(days=0, seconds=5),
                'iat': datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def __decode_auth_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, config['SECRET_KEY'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'