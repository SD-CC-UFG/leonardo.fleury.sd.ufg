import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_pymongo import PyMongo
from notes.database import get_db

bp = Blueprint('notes', __name__)

@bp.route('/', methods=['POST'])
def create_note():
    if request.is_json:
        note = request.json
        mongo = get_db()
        note = {'title': note['title'],
                'text': note['text'],
                'created': datetime.datetime.utcnow(),
                'last_updated': datetime.datetime.utcnow()}
        note_id = mongo.db.notes.insert_one(note).inserted_id
        return "{}".format(note_id)

    return "Not JSON"

@bp.route('/<uuid:note_id>', methods=['PUT'])
def update_note(note_id):
    with request.get_json as data:
        mongo = get_db()
        note = {'title': note['title'],
                'text': note['text'],
                'last_updated': datetime.datetime.utcnow()}
        mod_count = mongo.db.notes.update_one({'_id': note_id}, note).modified_count
        return "{} notes updated".format(mod_count)

@bp.route('/<uuid:note_id>', methods=['DELETE'])
def delete_note(note_id):
    mongo = get_db()
    del_count = mongo.db.notes.delete_one({'_id': note_id}).deleted_count
    return "Note deleted"
