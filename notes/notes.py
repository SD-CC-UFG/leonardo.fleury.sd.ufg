import datetime

from nameko.rpc import rpc
from bson.objectid import ObjectId
from bson.json_util import dumps
from notes.database import get_db


class Note(object):
    name = "notes"

    @rpc
    def create_note(self, title, text):
        mongo = get_db()
        # TODO: Document can be 16MB or less
        note = {'title': title,
                'text': text,
                'created': datetime.datetime.utcnow(),
                'last_updated': datetime.datetime.utcnow()}
        note_id = mongo.insert_one(note).inserted_id
        return dumps(note_id)

    @rpc
    def update_note(self, note_id, title, text):
        mongo = get_db()

        note = {'$currentDate': {'last_updated': True},
                '$set': {'title': title,
                         'text': text}}
        mod_count = mongo.update_one(
            {'_id': ObjectId(note_id)}, note).modified_count

        return dumps(mod_count)

    @rpc
    def delete_note(self, note_id):
        mongo = get_db()
        del_count = mongo.delete_one(
            {'_id': ObjectId(note_id)}).deleted_count
        return dumps(del_count)

    @rpc
    def view_note(self, note_id):
        mongo = get_db()

        note = mongo.find_one({"_id": ObjectId(note_id)})

        return dumps(note)

    @rpc
    def view_all_notes(self):
        mongo = get_db()

        notes = mongo.find()

        return dumps(notes)

    def __validate_note(self, note):
        pass