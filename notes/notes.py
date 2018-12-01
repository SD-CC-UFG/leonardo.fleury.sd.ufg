import datetime

from nameko.rpc import rpc
from bson.objectid import ObjectId
from notes.database import get_db


class Note(object):
    name = "notes"

    @rpc
    def create_note(self, title, text):
        mongo = get_db()
        note = {'title': title,
                'text': text,
                'created': datetime.datetime.utcnow(),
                'last_updated': datetime.datetime.utcnow()}
        note_id = mongo.db.notes.insert_one(note).inserted_id
        return "{}".format(note_id)

    @rpc
    def update_note(self, note_id, title, text):
        mongo = get_db()

        note = {'$currentDate': {'last_updated': True},
                '$set': {'title': title,
                         'text': text}}
        mod_count = mongo.db.notes.update_one(
            {'_id': ObjectId(note_id)}, note).modified_count

        return "{} notes updated".format(mod_count)

    @rpc
    def delete_note(self, note_id):
        mongo = get_db()
        del_count = mongo.db.notes.delete_one(
            {'_id': ObjectId(note_id)}).deleted_count
        return "{} note deleted".format(del_count)
