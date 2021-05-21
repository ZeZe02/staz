from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import *


class TeacherForm(FlaskForm):
    first_name = StringField(label='Jméno', validators=[DataRequired(), ])
    last_name = StringField(label='Přijmení', validators=[DataRequired(), ])
    login = StringField(label='Login', validators=[DataRequired(), ])
    manager = BooleanField(label='Manager')