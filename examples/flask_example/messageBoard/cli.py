import click
from flask.cli import with_appcontext

from .db import db
from .factories import MessageFactory

@click.command("populate_dev")
@with_appcontext
def populate_dev():
    MessageFactory.create_batch(size=4)