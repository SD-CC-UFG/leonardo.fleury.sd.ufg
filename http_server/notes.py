import logging
import json

from flask import current_app
from flask_restful import reqparse, abort, Resource
from nameko.standalone.rpc import ClusterRpcProxy

from http_server.auth import Auth

log = logging.getLogger(__name__)

class Note(Resource):
    def get(self, note_id):
        parser = reqparse.RequestParser()
        parser.add_argument('bearer', location='headers')
        args = parser.parse_args()

        username = Auth.decode_auth_token(args['bearer'])

        with ClusterRpcProxy(current_app.config) as rpc:
            note = rpc.notes.view_note(username, note_id)
            return note, 200
    
    def put(self, note_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('text', location='json')
        parser.add_argument('bearer', location='headers')
        args = parser.parse_args()
        
        username = Auth.decode_auth_token(args['bearer'])
        
        log.debug("Updating note:\n\t{}\n\t{}".format(args['title'], args['text']))

        with ClusterRpcProxy(current_app.config) as rpc:
            updated = rpc.notes.update_note(username, note_id, args['title'], args['text'])
            return updated, 200
    
    def delete(self, note_id):
        parser = reqparse.RequestParser()
        parser.add_argument('bearer', location='headers')
        args = parser.parse_args()

        username = Auth.decode_auth_token(args['bearer'])

        with ClusterRpcProxy(current_app.config) as rpc:
            deleted = rpc.notes.delete_note(username, note_id)
            return deleted, 200

class Notes(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('bearer', location='headers')
        args = parser.parse_args()

        username = Auth.decode_auth_token(args['bearer'])

        with ClusterRpcProxy(current_app.config) as rpc:
            notes = rpc.notes.view_all_notes(username)
            return notes, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('text', location='json')
        parser.add_argument('Bearer', location='headers')
        args = parser.parse_args()

        print("{}".format(args))
        username = Auth.decode_auth_token(args['Bearer'])

        log.debug("Creating note:\n\t{}\n\t{}".format(args['title'], args['text']))

        with ClusterRpcProxy(current_app.config) as rpc:
            note_id = rpc.notes.create_note(username, args['title'], args['text'])
            res = json.loads(note_id)

            if res['code'] is 0:
                return {
                    'note':{
                        'id': res['note_id']
                    }
                }, 200
            else:
                return {
                    'error': 'Some error'
                }, 500