from application import db
from sqlalchemy.sql import text
from application.models import Base



class Role(Base):

    roleName = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    ## roles
    roles_in_movies = db.relationship("PersonsRoleInMovie", back_populates="role")


    def __init__(self, roleName):
        self.roleName = roleName

    def get_role_list():
        return Role.query