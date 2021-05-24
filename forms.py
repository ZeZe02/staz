from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,DateField
from wtforms.validators import DataRequired,Email,EqualTo
from managers import *

class TeacherForm(FlaskForm):
    name  = StringField(label="Jméno", validators=[DataRequired("Povinné vyplnění!"), ])
    login = StringField(label="Login", validators=[DataRequired("Povinné vyplnění!"), ])
    #password1 = StringField(label="Heslo", validators=[DataRequired(), EqualTo("password2", "Hesla musí být stejná!")])
    #password2 = StringField(label="Opakování hesla")
    manager = BooleanField(label="Manager")



class ProjectForm(FlaskForm):
    title        = StringField(label="Název práce", validators=[DataRequired("Povinné vyplnění!"), ])
    supervisor   = StringField(label="Vedoucí práce", validators=[DataRequired("Povinné vyplnění!"), ])
    student      = SelectField(label="Jméno studenta", choices=StudentManager.choice_all_names() )
    class_exp    = StringField(label="Projekt pro třídu", validators=[DataRequired("Povinné vyplnění!"), ])
    school_year  = StringField(label="Školní rok", validators=[DataRequired("Povinné vyplnění!"), ])
    date_to      = DateField(label="Termín odevzdání")
"""
    classroom    = SelectField(label="Třída studenta", choices=ClassroomManager.choice_all_names() )

    grade_text = Optional(str)
    grade_list = Set("Project_criterion_grade")
    grade_final = Required("Type_grade")
    url1 = Optional(str)
    url2 = Optional(str)
    file_pdf = Required("File", reverse="project")
    file_attachment = Required("File", reverse="project_attachment")
    tags = Set("Tag")
    anotation = Optional(str)
    type_state = Required("Type_state")
"""