import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_pymongo import PyMongo
from notes.database import get_db

bp = Blueprint('notes', __name__)

@bp.route('/', methods=['POST'])
def create_note():
    pass

@bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    pass

@bp.route('/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    pass
