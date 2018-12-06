from flask import request
from flask_restful import Resource
from nameko.standalone.rpc import ClusterRpcProxy

class User(Resource):
    def get(self, user_id):
        pass
    
    def post(self, user_id, password):
        pass
    
    def put(self, user_id, old_password, new_password):
        pass
    
    def delete(self, user_id, password):
        pass