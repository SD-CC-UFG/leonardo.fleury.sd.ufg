from flask import current_app
from flask_restful import reqparse, abort, Resource
from nameko.standalone.rpc import ClusterRpcProxy


class User(Resource):
    def get(self, username):
        with ClusterRpcProxy(current_app.config) as rpc:
            user_id = rpc.users.view_user(username)
            return user_id, 200
    
    def put(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('password', location='json')
        parser.add_argument('new_password', location='json')
        args = parser.parse_args()

        with ClusterRpcProxy(current_app.config) as rpc:
            user_id = rpc.users.update_user_password(username, args['password'], args['new_password'])
            return user_id, 200
    
    def delete(self, username):
        with ClusterRpcProxy(current_app.config) as rpc:
            user_id = rpc.users.delete_user(username)
            return user_id, 200

class Users(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        args = parser.parse_args()

        with ClusterRpcProxy(current_app.config) as rpc:
            user_id = rpc.users.create_user(args['username'], args['password'])
            return user_id, 200