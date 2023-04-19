from featuremonkey import compose
from aspectlib import Aspect, weave, Proceed
from wtforms import StringField
from messageBoard.db import db

@Aspect
def addAuthorCard(_, **kwargs):
    yield Proceed("home_with_author.html", **kwargs)

@Aspect
def defaultAnon(self, res, **kwargs):
    if res.author == "":
        res.author = "Anonymous"
    yield Proceed(self, res, **kwargs)

class AuthorFormField:
    introduce_author = StringField("Author") 
    
class AuthorModelField:
    introduce_author = db.Column(db.String, nullable=False, default="Anonymous")

class AuthorTemplate:
    def refine_get(self, original):
        def get(cls):
            with weave("flask.render_template", addAuthorCard):
                return original(cls)
        
        return get

    def refine_post(self, original):
        def post(cls):
            with weave(db.session.add, defaultAnon):
                return original(cls)

        return post

def select(composer):
    from messageBoard.models.message import Message
    from messageBoard.views.home import MessageForm, HomeView

    composer.compose(AuthorFormField(), MessageForm)
    composer.compose(AuthorModelField(), Message)
    composer.compose(AuthorTemplate(), HomeView)