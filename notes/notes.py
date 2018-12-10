import datetime
import logging
import json

from nameko.rpc import rpc
from bson.objectid import ObjectId
from bson.json_util import dumps

from notes.database import get_db

log = logging.getLogger(__name__)

class Note(object):
    name = "notes"

    @rpc
    def create_note(self, user, title, text):
        mongo = get_db()
        # TODO: Document can be 16MB or less
        note = {'title': title,
                'text': text,
                'user_id': user,
                # 'created': datetime.datetime.utcnow(),
                'last_updated': datetime.datetime.utcnow()}

        note_id = mongo.insert_one(note).inserted_id

        log.info("{} created a note.".format(user))
        log.debug("{} created a note with id {}.".format(user, note_id))

        return json.dumps({
            "code": 0,
            "note_id": str(note_id)
        })

    @rpc
    def update_note(self, user, note_id, title, text):
        mongo = get_db(user)

        note = {'$currentDate': {'last_updated': True},
                '$set': {'title': title,
                         'text': text}}

        mod_count = mongo.update_one(
            {'_id': ObjectId(note_id)}, note).modified_count

        log.info("{} updated a note.".format(user))
        log.debug("Note {} from {} updated.".format(user, note_id))

        return json.dumps({
                    "code": 0,
                    "modified_count": mod_count
                })

    @rpc
    def delete_note(self, user, note_id):
        mongo = get_db(user)

        del_count = mongo.delete_one(
            {'_id': ObjectId(note_id)}).deleted_count

        log.info("{} deleted a note.".format(user))
        log.debug("Note {} from {} deleted.".format(user, note_id))

        return json.dumps({
                    "code": 0,
                    "deleted_count": del_count
                })

    @rpc
    def view_note(self, user, note_id):
        mongo = get_db(user)

        note = mongo.find_one({"_id": ObjectId(note_id)})

        return json.dumps({
                    "code": 0,
                    "note": {
                        "id": str(note["_id"]),
                        "title": note["title"],
                        "text": note["text"]
                    }
                })

    @rpc
    def view_all_notes(self, user):
        mongo = get_db(user)

        notes = mongo.find({'user_id': user})

        return dumps(notes)

    def __validate_note(self, note):
        pass
