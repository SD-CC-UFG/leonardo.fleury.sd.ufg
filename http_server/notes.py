from flask import request
from flask_restful import Resource
from nameko.standalone.rpc import ClusterRpcProxy

class Note(Resource):
    def get(self, note_id):
        pass
    
    def post(self, note_id, title, text):
        pass
    
    def put(self, note_id, title, text):
        pass
    
    def delete(self, note_id):
        pass

class Notes(Resource):
    def get(self):
        pass