from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,DateField,FileField,TextAreaField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired,Email,EqualTo
from managers import *

class TeacherForm(FlaskForm):
    name  = StringField(label="Jméno", validators=[DataRequired("Povinné vyplnění!"), ])
    login = StringField(label="Login", validators=[DataRequired("Povinné vyplnění!"), ])
    #password1 = StringField(label="Heslo", validators=[DataRequired(), EqualTo("password2", "Hesla musí být stejná!")])
    #password2 = StringField(label="Opakování hesla")
    manager = BooleanField(label="Manager")


class StudentForm(FlaskForm):
    login      = StringField(label="Login",    validators=[DataRequired("Povinné vyplnění!"), ])
    firstname  = StringField(label="Jméno",    validators=[DataRequired("Povinné vyplnění!"), ])
    surname    = StringField(label="Příjmení", validators=[DataRequired("Povinné vyplnění!"), ])
    #classroom    = SelectField(label="Třída studenta", choices=[(-1, "---")] + ClassroomManager.choice_all_names() )
    classroom    = SelectField(label="Třída studenta", choices=[(-1, "---")]  )



class ProjectForm(FlaskForm):
    title        = StringField(label="Název práce", validators=[DataRequired("Povinné vyplnění!"), ])
    supervisor   = StringField(label="Vedoucí práce", validators=[DataRequired("Povinné vyplnění!"), ])
    student      = SelectField(label="Jméno studenta", choices=[(-1, "---")] + StudentManager.choice_all_names() )
    class_exp    = StringField(label="Projekt pro třídu", validators=[DataRequired("Povinné vyplnění!"), ])
    school_year  = StringField(label="Rok", validators=[DataRequired("Povinné vyplnění!"), ])
    date_to      = DateField(label="Termín odevzdání", format="%d.%m.%Y")
   #classroom    = SelectField(label="Třída studenta", choices=[(-1, "---")] + ClassroomManager.choice_all_names() )
    classroom    = SelectField(label="Třída studenta", choices=[(-1, "---")]  )
    grade_text   = TextAreaField(label="Slovní hodnocení", validators=[DataRequired("Povinné vyplnění!"), ])
   #grade_final  = SelectField(label="Celkové hodnocení", choices=[(-1, "---")] + Type_gradeManager.choice_all_names() )
    grade_final  = SelectField(label="Celkové hodnocení", choices=[(-1, "---")]  )
    url1         = URLField(label="URL adresa 1" )
    url2         = URLField(label="URL adresa 2" )
    file_pdf        = FileField(label="Odevzdaná práce - PDF")
    file_attachment = FileField(label="Přílohy práce - ZIP")
    anotation    = TextAreaField(label="Anotace")
    #type_state   = SelectField(label="Status práce", choices=Type_stateManager.choice_all_names()  )
    type_state   = SelectField(label="Status práce", choices=[(-1, "---")]  )
