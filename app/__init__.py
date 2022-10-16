import flask_sqlalchemy
import flask
import flask.cli
import os

db = flask_sqlalchemy.SQLAlchemy()

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

def create_app(env=None) -> flask.Flask:
    from app.config import config_by_name
    
    app = flask.Flask(__name__)
    app.config.from_object(config_by_name[env or 'Testing'])    
    db.init_app(app)

    database_cli = flask.cli.AppGroup('database')
    @database_cli.command('init')
    def init_database():
        db.create_all()

    app.cli.add_command(database_cli)

    return app


