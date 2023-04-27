from flask.views import View
from flask import Blueprint, redirect

from messageBoard.db import db
from messageBoard.models.message import Message

bp = Blueprint("delete", __name__)

class Delete(View):
    def dispatch_request(self, id):
        row = Message.query.filter_by(id=id).first()
        db.session.delete(row)
        db.session.commit()
        return redirect("/")
    
bp.add_url_rule("/delete/<int:id>", view_func=Delete.as_view("delete"))
        