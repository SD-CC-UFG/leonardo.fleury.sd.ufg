import json
import jwt

from datetime import datetime, timedelta

from flask import current_app
from flask_restful import reqparse, abort, Resource
from nameko.standalone.rpc import ClusterRpcProxy

class Auth(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        args = parser.parse_args()

        with ClusterRpcProxy(current_app.config) as rpc:
            res = json.loads(rpc.auth.login(args['username'], args['password']))

            if res['code'] is 0:
                token = self.__encode_auth_token(args['username'])
                return token.decode('utf-8'), 200
            else:
                return 400
    
    def __encode_auth_token(self, username):
        try:
            payload = {
                'iss': 'notes auth server',
                'exp': datetime.utcnow() + timedelta(days=0, minutes=30, seconds=0),
                'iat': datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                current_app.config['JWT_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, current_app.config['JWT_KEY'])
            print(payload)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'