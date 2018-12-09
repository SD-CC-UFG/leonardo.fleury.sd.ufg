import json
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
            jwt = json.loads(rpc.auth.login(args['username'], args['password']))
            return jwt, 200