import os
from flask import Flask
from . import database
from . import main

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # TODO: Get key and database from env vars
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI="mongodb://admin:admin@localhost/admin"
    )

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

    # Registering database functionalits
    database.init_app(app)
    # Registering blueprints
    app.register_blueprint(main.bp)

    return app
