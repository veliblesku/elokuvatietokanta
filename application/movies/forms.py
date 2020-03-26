from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators

class MovieForm(FlaskForm):
    name = StringField("Movie name", [validators.Length(min=2)])
    duration = IntegerField("Movie duration")
    budget = FloatField("Movie budget")
    
    class Meta:
        csrf = False