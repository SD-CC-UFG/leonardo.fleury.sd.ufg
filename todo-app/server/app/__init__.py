from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    from .views import todo_page

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(todo_page)
    db.init_app(app)

    return app