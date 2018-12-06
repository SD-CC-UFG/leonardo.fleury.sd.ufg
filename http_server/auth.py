from flask import request
from flask_restful import Resource
from nameko.standalone.rpc import ClusterRpcProxy

class Auth(Resource):
    def get(self, username, password):
        pass