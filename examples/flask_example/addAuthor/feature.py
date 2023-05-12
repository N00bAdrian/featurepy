from featuremonkey import compose
from flask import render_template_string
from aspectlib import Aspect, weave, Proceed, Return
from wtforms import StringField
from bs4 import BeautifulSoup

from messageBoard.db import db

@Aspect
def addAuthorCard(filename, **kwargs):
    with open(f'messageBoard/templates/{filename}') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

        form = soup.find("form")
        author_form = soup.new_tag("div", attrs={
            "id": "author", 
            "class": "mb-3"
        })
        author_form.string = """{{form.author.label(class_="form-label")}}{{form.author(class_="form-control")}}"""
        form.find(id="title").insert_after(author_form)

        card = soup.find("div", class_="card-body")
        author_card = soup.new_tag("h6", attrs={
            "class": "card-subtitle text-body-secondary"
        })
        author_card.string = "{{msg.author}}"
        card.h5.insert_after(author_card)
        
        yield Return(render_template_string(soup.prettify(), **kwargs))

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
    from messageBoard.routes.home import MessageForm, HomeView

    composer.compose(AuthorFormField(), MessageForm)
    composer.compose(AuthorModelField(), Message)
    composer.compose(AuthorTemplate(), HomeView)