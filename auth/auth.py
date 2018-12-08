import jwt
import logging
import yaml

from datetime import datetime, timedelta

from nameko.rpc import rpc
from bson.json_util import dumps
from bcrypt import hashpw, gensalt

from auth.database import get_db

log = logging.getLogger(__name__)

class Auth(object):
    name = "auth"

    def __init__(self):
        # TODO: Set secret key in config file
        self.SECRET_KEY = 'somethingreallybighahahahahahahahahahahahahahaha'

    @rpc
    def login(self, username, password):
        mongo = get_db()

        user = mongo.find_one({'_id': username})

        if user:
            if (hashpw(password.encode('utf-8'), user['password']) == user['password']):
                token = self.__encode_auth_token(username)
                log.info("User was authenticate.")
                return {'code': 0, 'token': token}
            else:
                log.info("User was not authenticate.")
                return {'code': 1, 'error': 'Wrong username or password'}
        else:
            log.info("User was not authenticate.")
            return {'code': 1, 'error': 'Wrong username or password'}

    def __encode_auth_token(self, username):
        try:
            payload = {
                'iss': 'notes auth server',
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                self.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def __decode_auth_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, self.SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return {'code': 2, 'error': 'Signature expired. Please log in again.'}
        except jwt.InvalidTokenError:
            return {'code': 2, 'error': 'Invalid token. Please log in again.'}