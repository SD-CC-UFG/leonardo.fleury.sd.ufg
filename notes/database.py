from flask import current_app, g
from flask.cli import with_appcontext
from flask_pymongo import PyMongo


def get_db():
    if 'mongo' not in g:
        g.mongo = PyMongo(current_app)

    return g.mongo


def close_db(e=None):
    db = g.pop('mongo', None)

    if db is not None:
        db.cx.close()


def init_app(app):
    app.teardown_appcontext(close_db)
