from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.persons.models import Person
from application.roles.models import Role
from application.movies.models import Movie


class PersonsRoleInMovieForm(FlaskForm):
    movies = QuerySelectField(u'Movie', query_factory=Movie.get_movie_list, get_label='name')
    roles = QuerySelectField(u'Role', query_factory=Role.get_role_list, get_label='roleName')
    persons = QuerySelectField(u'Person', query_factory=Person.get_person_list, get_label='name')
    
    class Meta:
        csrf = False

    
class PersonsRoleInThisMovieForm(FlaskForm):
    movies = QuerySelectField(u'Movie', query_factory=Movie.get_movie_list, get_label='name')
    roles = QuerySelectField(u'Role', query_factory=Role.get_role_list, get_label='roleName')
    persons = QuerySelectField(u'Person', query_factory=Person.get_person_list, get_label='name')
    
    class Meta:
        csrf = False
    