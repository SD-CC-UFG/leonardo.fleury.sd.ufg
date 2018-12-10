import logging

from flask import current_app, json
from flask_restful import reqparse, abort, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from nameko.standalone.rpc import ClusterRpcProxy

from http_server.auth import Auth

log = logging.getLogger(__name__)


class Note(Resource):
    @jwt_required
    def get(self, note_id):
        username = get_jwt_identity()

        with ClusterRpcProxy(current_app.config) as rpc:
            note = json.loads(rpc.notes.view_note(username, note_id))
            return {
                'note': note["note"]
            }, 200

    @jwt_required
    def put(self, note_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('text', location='json')
        args = parser.parse_args()

        username = get_jwt_identity()

        log.debug("Updating note:\n\t{}\n\t{}".format(
            args['title'], args['text']))

        with ClusterRpcProxy(current_app.config) as rpc:
            updated = rpc.notes.update_note(
                username, note_id, args['title'], args['text'])
            if updated:
                return {
                    'success': 'Note updated'
                }, 200
            else:
                return {
                    'error': 'Note could note be updated'
                }, 500

    @jwt_required
    def delete(self, note_id):
        username = get_jwt_identity()

        with ClusterRpcProxy(current_app.config) as rpc:
            deleted = rpc.notes.delete_note(username, note_id)
            if deleted:
                return {
                    'success': 'Note was deleted'
                }, 200
            else:
                return {
                    'error': 'Note could not be deleted'
                }, 500


class Notes(Resource):
    @jwt_required
    def get(self):
        username = get_jwt_identity()

        with ClusterRpcProxy(current_app.config) as rpc:
            notes = json.loads(rpc.notes.view_all_notes(username))
            return {
                'notes': notes
            }, 200

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('text', location='json')
        args = parser.parse_args()

        username = get_jwt_identity()

        log.debug("Creating note:\n\t{}\n\t{}".format(
            args['title'], args['text']))

        with ClusterRpcProxy(current_app.config) as rpc:
            note_id = rpc.notes.create_note(
                username, args['title'], args['text'])
            res = json.loads(note_id)

            if res['code'] is 0:
                return {
                    'note': {
                        'id': res['note_id']
                    }
                }, 200
            else:
                return {
                    'error': 'Some error'
                }, 500
