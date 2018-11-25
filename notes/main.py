import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_pymongo import PyMongo
from notes.database import get_db

bp = Blueprint('notes', __name__)

@bp.route('/', methods=['POST'])
def create_note():
    mongo = get_db()

    note = {"title": "Test note",
            "text": "Testing the database connection hehe",
            "date": datetime.datetime.utcnow()}

    note_id = mongo.db.notes.insert_one(note).inserted_id
    return "200 Ok"

@bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    pass

@bp.route('/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    pass
