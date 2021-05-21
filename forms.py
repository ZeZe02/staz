from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class Teacher_form(FlaskForm):
    name = StringField(label='Jméno')
    login = StringField(label='login')
    manager = BooleanField(label='Manager')
