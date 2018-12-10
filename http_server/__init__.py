import os
import yaml
import logging

from flask import Flask
from flask_restful import Api

from http_server.notes import Note, Notes
from http_server.users import User, Users
from http_server.auth import Auth

log = logging.getLogger(__name__)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # TODO: Get secret_key from config.yaml
    app.config.from_mapping(
        SECRET_KEY='dev',
        AMQP_URI='pyamqp://guest:guest@localhost',
        JWT_KEY='secret_jwt_key')

    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        try:
            app.config.from_pyfile("config.cfg")
        except IOError as e:
            log.error("Error loading configuration file.")
            log.error(e)
    else:
        # load the test config if passed in
        log.info("Loading test configurations")
        app.config.from_mapping(test_config)

    api.add_resource(Notes, '/notes')
    api.add_resource(Note, '/note/<note_id>')
    api.add_resource(Users, '/user')
    api.add_resource(User, '/user/<username>')
    api.add_resource(Auth, '/auth')

    return app
