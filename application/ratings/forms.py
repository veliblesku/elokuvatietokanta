from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators

class MovieRatingForm(FlaskForm):
    rating = FloatField("Movie Rating")
    
    class Meta:
        csrf = False