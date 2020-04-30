from application import db
from sqlalchemy.sql import text
from application.models import Base


class Person(Base):

    name = db.Column(db.String(144), nullable=False)
    birthday = db.Column(db.Date, nullable=True)

    roles_in_movies = db.relationship("PersonsRoleInMovie", back_populates="person")



    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    @staticmethod
    def get_person_list():
        return Person.query
