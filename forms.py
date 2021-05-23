from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo

class TeacherForm(FlaskForm):
    name  = StringField(label="Jméno", validators=[DataRequired("Povinné vyplnění!"), ])
    login = StringField(label="Login", validators=[DataRequired("Povinné vyplnění!"), ])
    #password1 = StringField(label="Heslo", validators=[DataRequired(), EqualTo("password2", "Hesla musí být stejná!")])
    #password2 = StringField(label="Opakování hesla")
    manager = BooleanField(label="Manager")
