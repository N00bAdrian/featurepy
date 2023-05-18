from featurepy.flask import FView
from flask import Blueprint

from messageBoard.db import db
from messageBoard.models.message import Message

bp = Blueprint("delete", __name__)

class Delete(FView):
    def dispatch_request(self, id):
        row = Message.query.filter_by(id=id).first()
        db.session.delete(row)
        db.session.commit()
        return self.redirect("/")
    
bp.add_url_rule("/delete/<int:id>", view_func=Delete.as_view("delete"))
        