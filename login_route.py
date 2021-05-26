from app import app
from flask import session, flash, redirect, url_for, render_template, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

from pony.orm import db_session
from ldap3 import Server, Connection, ALL, NTLM
from models import Student, Teacher, Classroom
import re


class LoginForm(FlaskForm):
    login = StringField("login", validators=[InputRequired()])
    passwd = PasswordField("passwd", validators=[InputRequired()])
    submit = SubmitField("login_me")


@app.route("/login/", methods=["GET", "POST"])
@db_session
def login():
    if "user" in session:
        flash("Už jsi přihlášen!")
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        passwd = form.passwd.data

        # server = Server("pdc.spseol.cz", get_info=ALL)
        server = Server("172.24.1.1", get_info=ALL)
        conn = Connection(
            server,
            user="spseol.cz\\{}".format(login),
            password=passwd,
            authentication=NTLM,
        )
        if app.env == "development" or conn.bind():
            if app.env == "development":
                name = login
                login = "." + login
                classname = "develop"
            else:
                conn.search(
                    "dc=spseol,dc=cz",
                    f"(sAMAccountName={login})",
                    attributes=["cn", "distinguishedName"],
                )
                m = re.search(
                    "OU=([1234]([ABCL]|V[TE]))",
                    conn.entries[-1].distinguishedName.value.upper(),
                )
                if m:
                    classname = m.group(1)
                else:
                    classname = "XxX"
                name = conn.entries[-1].cn.value
            classroom = Classroom.get(name=classname) or Classroom(name=classname)
            if re.search(r"^\.?\w{3}\d{5}$", login):
                student = Student.get(login=login)
                session["role"] = "student"
                if student:
                    student.classroom = classroom
                else:
                    student = Student(
                        login=login, firstname=name, surname=".", classroom=classroom
                    )
            else:
                teacher = Teacher.get(login=login)
                session["role"] = "teacher"
                if not teacher:
                    teacher = Teacher(login=login, name=name)
            conn.unbind()
            session["user"] = login
            session["name"] = name
            flash("Právě jsi se přihlásil!")
            next_ = request.args.get("next")
            if next_:
                print(next_)
                return redirect(next_)
            else:
                return redirect(url_for("index"))
        else:
            flash("Špatné přihlašovací údaje!")
            return redirect(url_for("login"))
    return render_template("login.html", title="LogIn", form=form)


@app.route("/logout/")
def logout():
    session.pop("user", None)
    session.pop("role", None)
    session.pop("name", None)
    flash("Byl jsi odhlášen!")
    return redirect(url_for("login"))
