from flask import Flask
from flask_bootstrap import Bootstrap5

from .routes import home
from .db import db, migrate
from .models.message import Message
from .factories.messageFactory import MessageFactory
from .cli import populate_dev


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    bootstrap = Bootstrap5(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home.bp)
    app.cli.add_command(populate_dev)

    return app
