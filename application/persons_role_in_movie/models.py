from application import db
from sqlalchemy.sql import text
from application.models import Base


class PersonsRoleInMovie(Base):
    
    __tablename__ = "roles_in_movies"
    
    movie_id= db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    role_id =  db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    person_id =  db.Column(db.Integer, db.ForeignKey('person.id'), nullable=True)

    __table_args__ = (db.UniqueConstraint(movie_id, role_id, person_id),)
    ## roles
    role = db.relationship("Role", back_populates="roles_in_movies")
    ## movie
    movie = db.relationship("Movie", back_populates="roles_in_movies")
    ## person
    person = db.relationship("Person", back_populates="roles_in_movies")




    @staticmethod
    def get_credits(movie_id):
        stmt = text("SELECT rim.id, p.name, r.roleName FROM roles_in_movies rim JOIN person p ON rim.person_id = p.id JOIN role r ON rim.role_id=r.id  WHERE movie_id=:m_id;").params(m_id=movie_id);
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "person":row[1], "role":row[2]})
        return response