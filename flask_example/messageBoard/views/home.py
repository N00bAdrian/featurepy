from flask.views import MethodView
from flask import Blueprint, render_template

bp = Blueprint("home", __name__, template_folder="../templates")

class HomeView(MethodView):

    def get(self):
        return render_template("home.html")

bp.add_url_rule("/", view_func=HomeView.as_view("home"))