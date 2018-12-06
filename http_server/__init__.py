import os

from flask import Flask
from flask_restful import Api

from http_server.notes import Note, Notes
from http_server.users import User
from http_server.auth import Auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev') # TODO: Get secret_key from config.yaml

    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api.add_resource(Notes, '/notes')
    api.add_resource(Note, '/notes/<note_id>')
    api.add_resource(User, '/user/<user_id>')
    api.add_resource(Auth, '/auth')

    return app