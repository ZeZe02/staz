from flask import Flask, render_template, request, flash, redirect, url_for
from pony.flask import Pony
from models import *
from managers import *
from forms import *

app = Flask(__name__)
Pony(app)
#musí být, pokud se pracuje s cookies
app.secret_key = "sdfsdfsdgsdfgsadfg"

@app.route('/')
def hello_world():
    return render_template("index.html",pozdrav="Ahoj",cisla=range(0,9))

@app.route('/ucitel/', methods=["GET", "POST"])
def teacher():
    msg = ""
    if request.method == "POST":
        fname = request.form.get("fname","")
        lname = request.form.get("lname","")
        login = request.form.get("login","")
        manager = request.form.get("manager","")
        fullname = f"{fname} {lname}"
        teacher = TeacherManager.create_teacher(fullname, login, manager)
        flash("Vytvořeno!")
        return redirect(url_for("teacher"))
    return render_template("teacher.html",msg=msg)

@app.route('/ucitel_wtf/', methods=["GET", "POST"])
def teacher_wtf():
    form = TeacherForm()
    if request.method == "POST":
        if form.validate():
            fname = form.data.get("fname")
            sname = form.data.get("sname")
            login = form.data.get("login")
            manager = form.data.get("manager")
            fullname = f"{fname} {sname}"
            teacher = TeacherManager.create_teacher(fullname, login, manager)
            flash("Vytvořeno!")
            return redirect(url_for("teacher_wtf"))
    return render_template("teacher_wtf.html",form=form)


@app.route('/seznam_ucitelu/')
def list_of_teachers():
    teachers = TeacherManager.GetTeachers()
    return render_template("list_of_teachers.html", teachers=teachers)

@app.route('/smazat_ucitele/', methods=["GET", "POST"])
def smazat_ucitele():
    id=request.form.get("smazat")
    if id!= None:
        TeacherManager.delete_teacher(id)
    return redirect(url_for("list_of_teachers"))

@app.route('/upravit_ucitele/<id>/', methods=["GET", "POST"])
def upravit_ucitele():
    if request.method == "POST":
        form = TeacherForm() # zde dojde k předání všech hodnot formuláře postem
        if form.validate():
            TeacherManager.update_teacher(TeacherManager.get_teacher(id),
                                               login=form.data.get("login"),
                                               name=form.data.get("name"),
                                               manager=form.data.get("manager"))
            flash("Změny uloženy")
            return redirect(url_for("list_of_teachers"))
        flash("Chybně vyplněno, změny neuloženy")
    else:
        t = TeacherManager.get_teachar(id)
        form = TeacherForm(login=t.login, name=t.name, manager=t.manager)
    return render_template("teacher-edit.html", form=form)

@app.route('/znamka/', methods=["GET", "POST"])
def grade():
    msg = ""
    if request.method == "POST":
        name = request.form.get("name","")
        order = request.form.get("order","")
        grade = create_grade(order, name)
        flash("Vytvořeno!")
        return redirect(url_for("grade"))
    return render_template("grade.html",msg=msg)


@app.route('/ucitele/<name>/')
def hello_teachers(name):
    return f'Hello Teacher {name}!'

if __name__ == '__main__':
    app.run()
