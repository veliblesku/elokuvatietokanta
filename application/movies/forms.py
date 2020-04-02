from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class MovieForm(FlaskForm):
    name = StringField("Movie name", [validators.Length(min=2)])
    duration = IntegerField("Movie duration")
    budget = FloatField("Movie budget")
    year = IntegerField("Movie year")

    
    class Meta:
        csrf = False


