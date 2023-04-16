from flask import Flask
from flask_bootstrap import Bootstrap5
from .views import home

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    app.register_blueprint(home.bp)

    return app