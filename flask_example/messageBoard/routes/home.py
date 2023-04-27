from flask.views import MethodView
from flask import Blueprint, request, redirect
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired
from sqlalchemy import select

import flask

from ..db import db
from ..models.message import Message

bp = Blueprint("home", __name__, template_folder="../templates")

class MessageForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])

class HomeView(MethodView):

    def get(self):
        form = MessageForm(request.form)
        messages = db.session.execute(select(Message)).scalars().all()
        return flask.render_template("home.html", form=form, messages=messages)

    def post(self):
        form = MessageForm(request.form)
        if form.validate():
            print("Form validated")
            db.session.add(Message(**form.data))
            db.session.commit()
        
        return redirect("/")

bp.add_url_rule("/", view_func=HomeView.as_view("home"))