from ..db import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)