from application import db
from sqlalchemy.sql import text



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Float, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    ratings = db.relationship("Rating", backref='movie', lazy=True)

    def __init__(self, name, duration, budget):
        self.name = name
        self.duration = duration
        self.budget = budget



    
    def find_movie_avg(account_id, movie_id):
        exists = text("SELECT EXISTS"
                        "(SELECT * FROM rating WHERE account_id=:a_id AND movie_id=:m_id)").params(a_id=account_id, m_id=movie_id);

        stmt = text("SELECT avg(rating) FROM rating"
                " WHERE movie_id=:id").params(id=movie_id);

        res = db.engine.execute(stmt)
        response = []
        print("moro")
        print(res)
        for row in res:
            response.append(row[0])
        print(response[0])
        return response[0]