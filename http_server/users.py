import logging

from flask import current_app, json
from flask_restful import reqparse, abort, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from nameko.standalone.rpc import ClusterRpcProxy

log = logging.getLogger(__name__)


class User(Resource):
    @jwt_required
    def get(self, username):
        jwt_identity = get_jwt_identity()

        if username == jwt_identity:
            with ClusterRpcProxy(current_app.config) as rpc:
                user_id = json.loads(rpc.users.view_user(username))
                return {
                    'user': {
                        'id': user_id
                    }
                }, 200
        else:
            return {'error': 'You dont have permision to be here.'}

    @jwt_required
    def put(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('password', location='json')
        parser.add_argument('new_password', location='json')
        args = parser.parse_args()

        jwt_identity = get_jwt_identity()

        if username == jwt_identity:
            with ClusterRpcProxy(current_app.config) as rpc:
                changed = json.loads(rpc.users.update_user_password(
                    username, args['password'], args['new_password']))
                if changed:
                    return {'success': 'Password changed'}, 200
                else:
                    return {'error': 'Password could not be changed'}, 500
        else:
            return {'error': 'You dont have permision to be here.'}, 300

    @jwt_required
    def delete(self, username):
        jwt_identity = get_jwt_identity()

        if username == jwt_identity:
            with ClusterRpcProxy(current_app.config) as rpc:
                deleted = json.loads(rpc.users.delete_user(username))
                if deleted:
                    return {'success': 'User deleted'}, 200
                else:
                    return {'error': 'User could not be deleted'}, 500
        else:
            return {'error': 'You dont have permision to be here.'}, 300


class Users(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        args = parser.parse_args()

        with ClusterRpcProxy(current_app.config) as rpc:
            user_id = json.loads(rpc.users.create_user(
                args['username'], args['password']))
            return {
                'user': {
                    'id': user_id
                }
            }, 200
