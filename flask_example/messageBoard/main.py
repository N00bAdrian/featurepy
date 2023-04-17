from flask import Flask
from flask_bootstrap import Bootstrap5

from .views import home
from .db import db
from .models.message import Message
from .factories.messageFactory import MessageFactory

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    bootstrap = Bootstrap5(app)

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        MessageFactory.create_batch(size=4)

    app.register_blueprint(home.bp)

    return app