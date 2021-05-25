from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import *


class TeacherForm(FlaskForm):
    fname = StringField(label='Jméno', validators=[DataRequired(), ])
    lname = StringField(label='Přijmení', validators=[DataRequired(), ])
    login = StringField(label='Login', validators=[DataRequired(), ])
    manager = BooleanField(label='Manager')

class GradeForm(FlaskForm):
    name = StringField(label='Jméno známky', validators=[DataRequired(), ])
    order = StringField(label='Pořadí známky', validators=[DataRequired(), ])

class ProjectForm(FlaskForm):
    title = StringField(label="Název práce", validators=[DataRequired(), ])
    supervisor = StringField(label="Vedoucí práce", validators=[DataRequired(), ])
    classroom = StringField(label = "Třída", validators=[DataRequired(), ])
    type_state = BooleanField(label="Volné")