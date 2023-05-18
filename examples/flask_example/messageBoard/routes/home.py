from flask import Blueprint, request
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired
from sqlalchemy import select

from featurepy.flask import FMethodView

from ..db import db
from ..models.message import Message

bp = Blueprint("home", __name__, template_folder="../templates")

class MessageForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])

class HomeView(FMethodView):
    @staticmethod
    def add_to_db(data):
        db.session.add(Message(**data))
        db.session.commit()

    def get(self):
        form = MessageForm(request.form)
        messages = db.session.execute(select(Message)).scalars().all()
        return self.render("home.html", form=form, messages=messages)

    def post(self):
        form = MessageForm(request.form)
        if form.validate():
            print("Form validated")
            # db.session.add(Message(**form.data))
            # db.session.commit()
            self.add_to_db(form.data)
        
        return self.redirect("/")

bp.add_url_rule("/", view_func=HomeView.as_view("home"))