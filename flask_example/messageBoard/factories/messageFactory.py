from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory
from faker.providers import lorem, person, python

from ..db import db
from ..models.message import Message

Faker.add_provider(python)
Faker.add_provider(lorem)
Faker.add_provider(person)

class MessageFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Message
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    title = Faker("text", max_nb_chars=15)
    message = Faker("paragraph", nb_sentences=2)