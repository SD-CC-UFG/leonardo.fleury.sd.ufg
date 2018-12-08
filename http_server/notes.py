import logging

from flask import current_app
from flask_restful import reqparse, abort, Resource
from nameko.standalone.rpc import ClusterRpcProxy

log = logging.getLogger(__name__)

class Note(Resource):
    def get(self, note_id):
        with ClusterRpcProxy(current_app.config) as rpc:
            note = rpc.notes.view_note('user', note_id)
            return note, 200
    
    def put(self, note_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('text', location='json')
        args = parser.parse_args()

        log.debug("Updating note:\n\t{}\n\t{}".format(args['title'], args['text']))

        with ClusterRpcProxy(current_app.config) as rpc:
            updated = rpc.notes.update_note('user', note_id, args['title'], args['text'])
            return updated, 200
    
    def delete(self, note_id):
        with ClusterRpcProxy(current_app.config) as rpc:
            deleted = rpc.notes.delete_note('user', note_id)
            return deleted, 200

class Notes(Resource):
    def get(self):
        with ClusterRpcProxy(current_app.config) as rpc:
            notes = rpc.notes.view_all_notes('user')
            return notes, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('text', location='json')
        args = parser.parse_args()

        log.debug("Updating note:\n\t{}\n\t{}".format(args['title'], args['text']))

        with ClusterRpcProxy(current_app.config) as rpc:
            note_id = rpc.notes.create_note('user', args['title'], args['text'])
            return note_id, 200