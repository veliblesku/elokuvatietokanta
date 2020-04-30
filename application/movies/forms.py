from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.roles.models import Role
from application.movies.models import Movie


class MovieForm(FlaskForm):
    name = StringField("Movie name", [validators.Length(min=2)])
    duration = IntegerField("Movie duration")
    budget = FloatField("Movie budget")
    year = IntegerField("Movie year")

    
    class Meta:
        csrf = False


