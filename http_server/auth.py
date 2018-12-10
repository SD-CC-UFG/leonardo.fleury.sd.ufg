from datetime import timedelta

from flask import current_app, json
from flask_restful import reqparse, abort, Resource
from flask_jwt_extended import create_access_token
from nameko.standalone.rpc import ClusterRpcProxy


class Auth(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        args = parser.parse_args()

        with ClusterRpcProxy(current_app.config) as rpc:
            res = json.loads(rpc.auth.login(
                args['username'], args['password']))

            if res['code'] is 0:
                expiration_time = timedelta(
                    days=0, hours=12, minutes=0, seconds=0, microseconds=0)
                token = create_access_token(
                    identity=args['username'], expires_delta=expiration_time)
                return {
                    'token': token
                }, 200
            else:
                return 400
