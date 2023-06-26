from wtforms import StringField
from bs4 import BeautifulSoup
from tempfile import NamedTemporaryFile
from os import path
from flask import request
from featurepy import Aspect, Proceed, weave

from messageBoard.db import db
from messageBoard.routes.home import MessageForm


def _add_author_form(soup):
    form = soup.find("form")
    author_form = soup.new_tag("div", attrs={
        "id": "author",
        "class": "mb-3"
    })
    author_form.string = """{{form.author.label(class_="form-label")}}{{form.author(class_="form-control")}}"""
    form.find(id="title").insert_after(author_form)

    return soup


def _add_author_card(soup):
    card = soup.find("div", class_="card-body")
    author_card = soup.new_tag("h6", attrs={
        "class": "card-subtitle text-body-secondary"
    })
    author_card.string = "{{msg.author}}"
    card.h5.insert_after(author_card)

    return soup


@Aspect
def add_author_template(filename, **kwargs):
    with open(f'messageBoard/templates/{filename}') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        soup = _add_author_form(soup)
        soup = _add_author_card(soup)

        with NamedTemporaryFile(suffix=".html", dir="messageBoard/templates") as tfp:
            tfp.write(str.encode(soup.prettify()))
            tfp.seek(0)
            yield Proceed(path.basename(tfp.name), **kwargs)


def empty_to_anonymous(form, field):
    field.data = "Anonymous" if field.data == "" else field.data


class AuthorFormField:
    introduce_author = StringField("Author", validators=[empty_to_anonymous])


class AuthorModelField:
    introduce_author = db.Column(
        db.String, nullable=False, default="Anonymous")


class AuthorViewField:
    def refine_get(self, original):
        def get(slf):
            with weave("flask.render_template", add_author_template):
                return original(slf)
        return get


def select(composer):
    from messageBoard.models.message import Message
    from messageBoard.routes.home import MessageForm, HomeView

    composer.compose(AuthorFormField(), MessageForm)
    composer.compose(AuthorModelField(), Message)
    # composer.compose(AuthorViewField(), HomeView)
    HomeView.register_aspect(
        "get", "flask.render_template", add_author_template)
