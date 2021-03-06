from application import db
from sqlalchemy.sql import text
from application.models import Base



class Movie(Base):

    name = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    ratings = db.relationship("Rating", backref='movie', lazy=True)

    roles_in_movies = db.relationship("PersonsRoleInMovie", back_populates="movie", lazy=True)



    def __init__(self, name, duration, budget, year):
        self.name = name
        self.duration = duration
        self.budget = budget
        self.year = year

    @staticmethod
    def get_movie_list():
        return Movie.query

    @staticmethod
    def get_movie_makers():

        return 0;
        return Movie.query