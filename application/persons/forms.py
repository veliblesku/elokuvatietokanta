from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, validators
from wtforms.fields.html5 import DateField
from datetime import date
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class PersonForm(FlaskForm):
    name = StringField("Person Name", [validators.Length(min=2, max=40)])
    dateOfBirth = DateField("Date of Birth",default=date.today)

    class Meta:
        csrf = False


