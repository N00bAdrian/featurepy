from flask.views import MethodView
from flask import Blueprint, render_template
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired
from sqlalchemy import select

from ..db import db
from ..models.message import Message

bp = Blueprint("home", __name__, template_folder="../templates")

class MessageForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])

class HomeView(MethodView):

    def get(self):
        form = MessageForm()

        messages = db.session.execute(select(Message)).scalars().all()

        return render_template("home.html", form=form, messages=messages)

bp.add_url_rule("/", view_func=HomeView.as_view("home"))