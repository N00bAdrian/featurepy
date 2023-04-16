from flask.views import MethodView
from flask import Blueprint, render_template

bp = Blueprint("home", __name__, template_folder="../templates")

class HomeView(MethodView):

    def get(self):
        messages = [
            {
                "title": "Title 1",
                "message": "This is a message"
            },
            {
                "title": "Title 2",
                "message": "This is also a message"
            },
            {
                "title": "Title 3",
                "message": "This is also a message"
            },
            {
                "title": "Title 4",
                "message": "This is also a message"
            },
        ]

        return render_template("home.html", messages=messages)

bp.add_url_rule("/", view_func=HomeView.as_view("home"))