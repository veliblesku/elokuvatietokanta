from application import db
from sqlalchemy.sql import text
from application.models import Base

class Rating(Base):

    rating = db.Column(db.Integer(), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __init__(self, rating):
        self.rating = rating
    


    @staticmethod
    def find_movie_avg(movie_id):
        stmt = text("SELECT avg(rating) FROM rating"
                " WHERE movie_id=:id").params(id=movie_id);


        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        print(response[0])
        return response[0]

    @staticmethod
    def user_has_rated(account_id, movie_id):
        exists = text("SELECT EXISTS"
                "(SELECT * FROM rating WHERE account_id=:a_id AND movie_id=:m_id)").params(a_id=account_id, m_id=movie_id);

        res = db.engine.execute(exists)
        response = []
        for row in res:
            response.append(row[0])
        print("novoivittu")
        print(response[0])
        print("voimoro")
        return response[0]
    
    @staticmethod
    def find_movies_user_has_rated(account_id):
        stmt = text("SELECT Movie.name, Movie.year, Rating.rating FROM movie LEFT JOIN rating ON Movie.id=rating.movie_id WHERE rating.account_id =:a_id;").params(a_id=account_id);
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "year":row[1], "rating": row[2]})
        print(response)
        return response

    @staticmethod
    def check_if_user_has_rated_movie(account_id, movie_id):
        stmt = text("SELECT Rating.id FROM rating WHERE account_id=:a_id AND movie_id=:m_id;").params(a_id=account_id, m_id=movie_id);
        res = db.engine.execute(stmt)
        print("RES ON = = = = ")
        print(res)
        print("RESEIERWREASJFDS")
        response = []
        for row in res:
            response.append(row[0])
        return response