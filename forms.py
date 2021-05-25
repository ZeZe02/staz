from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import *

class TeacherForm(FlaskForm):
    fname = StringField(label="Jméno", validators=[DataRequired()])
    sname = StringField(label="Příjmení", validators=[DataRequired()])
    login = StringField(label="Login", validators=[DataRequired()])
    manager = BooleanField(label="Manažer")

