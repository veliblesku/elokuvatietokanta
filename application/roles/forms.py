from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.persons.models import Person
from application.roles.models import Role

class RoleForm(FlaskForm):
    rolename = StringField("Role in movie", [validators.Length(min=2)])

    
    class Meta:
        csrf = False

class RoleFormAddPersonInMovie(FlaskForm):
    roles = QuerySelectField(u'Role', query_factory=Role.get_role_list, get_label='rolename')
    persons = QuerySelectField(u'Person', query_factory=Person.get_person_list, get_label='name')
    

