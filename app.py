from flask import Flask, render_template, request, url_for, redirect, flash, Response
from pony.flask import Pony
from pony.orm import commit, db_session
#import models
from models import *
from managers import *
from forms import *

app = Flask(__name__)
app.secret_key = "asfuogasdhkjfbvasdhjkcbvdasjhk,56789"
Pony(app)


# ukazka definice vlastniho dekoratoru @calculate_time
import time
def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.name, end - begin)
        return result

    return inner1

@db_session
@app.route('/')
#@calculate_time
def index():
    """
    u = Teacher(name="Igor",login="igor")
    commit()  # asi zde není potřeba, protože ten dekorátor db_session zajistí, že celá tato funkce bude brána jako jedna transakce a commitne se automaticky na konci funkce
    """
    jmeno = "" #Teacher.get(id=1).name   # tohle ještě nezpůsobí SQL dotaz do DB, ale nachystá si to a až při použití té proměnné jmeno ten dotaz proběhne
    pracejednicky = "" #Teacher.get(id=1).projects

    return render_template("index.html",jmeno=jmeno,pracejednicky=pracejednicky)


@app.route("/ucitel/", methods = ["GET", "POST"])
def ucitel():
    if request.method == "POST":
        login = request.form.get("login")
        jmeno = request.form.get("fname")
        prijm = request.form.get("lname")
        manager = request.form.get("manager")
        fullname = f"{jmeno} {prijm}"
        t = TeacherManager.create_teacher(login=login, name=fullname, manager=manager)
        flash(f"Úspěšně přidán učitel {fullname} manager={manager}")  # nachystá do zásobníku (v rámci cookies) tuto "hlášku" a šablona base si ji pak použije
        # v ramci requestu se da detekovat i mobil - request z mobilniho telefonu
        # dat sem breakpoint a pak inspekovat request
        return redirect(url_for("ucitel"))
    return render_template("teacher-add.html")

@app.route("/ucitelWTF/", methods = ["GET", "POST"])
def teacher_add():
    form = TeacherForm()
    if request.method == "POST":
        if form.validate():
            t = TeacherManager.create_teacher(login=form.data.get("login"),
                                              name=form.data.get("name"),
                                              manager=form.data.get("manager"))
            flash(f"Úspěšně přidán učitel {form.data.get('name')} manager={form.data.get('manager')}")  # nachystá do zásobníku (v rámci cookies) tuto "hlášku" a šablona base si ji pak použije
            return redirect(url_for("teacher_add"))
        else:
            flash("Chyba při přidání učitele!")
    return render_template("teacher-add-WTF.html", form=form)

@app.route('/ucitel-smazat/<id>/')
def teacher_del(id):
    tm = TeacherManager.delete_teacher(id)
    flash(f"Učitel smazán")
    return redirect(url_for("teachers"))

@app.route('/ajax-teacher-delete/', methods=["POST"])
def teacher_del1():
    id = request.form.get("id")
    response = Response()
    response.set_data('')
    if id:
        tm = TeacherManager.delete_teacher(id)
        flash(f"Učitel smazán")
        response.status=200
        return response
    response.status=500
    return response

@app.route('/ucitele/<id>/', methods = ["GET", "POST"])
def teacher_edit(id):
    if request.method == "POST":
        form = TeacherForm()
        if form.validate():
            tm = TeacherManager.update_teacher(TeacherManager.get_teacher(id), **form.data )   # pouzito **kwargs
            #tm = TeacherManager.update_teacher(TeacherManager.get_teacher(id),
            #                                   login=form.data.get("login"),
            #                                   name=form.data.get("name"),
            #                                   manager=form.data.get("manager"))
            flash(f"Změny úspěšně uloženy")
            return redirect(url_for("teachers"))
        flash("Chybně vyplněný formulář, změny neuloženy!")
    else:
        t = TeacherManager.get_teacher(id)
        form = TeacherForm(login=t.login, name=t.name, manager=t.manager)
    return render_template("teacher-edit.html", form=form)

@app.route('/ucitele/')
def teachers():
    teachers_list = TeacherManager.get_teachers()
    return render_template("teachers-list.html", teachers = teachers_list)


@app.route("/student-novy/", methods = ["GET", "POST"])
def student_add():
    form = StudentForm()
    if request.method == "POST":
        if form.validate():
            t = StudentManager.create_one( **form.data )
            flash(f"Úspěšně přidán student {form.data.get('login')}")
            return redirect(url_for("student_add"))
        else:
            flash("Chyba při přidání studenta!")
    return render_template("student-add.html", form=form)

@app.route('/ajax-student-delete/', methods=["POST"])
def student_del():
    id1 = request.form.get("id")
    response = Response()
    response.set_data('')
    if id1:
        tm = StudentManager.delete_one(id1)
        flash(f"Student smazán")
        response.status=200
        return response
    response.status=500
    return response

@app.route('/studenti/<id>/', methods = ["GET", "POST"])
def student_edit(id):
    if request.method == "POST":
        form = StudentForm()
        if form.validate():
            tm = StudentManager.update_one(StudentManager.get_one(id), **form.data )
            flash(f"Změny úspěšně uloženy")
            return redirect(url_for("students"))
        flash("Chybně vyplněný formulář, změny neuloženy!")
    else:
        t = StudentManager.get_one(id)
        form = StudentForm(login=t.login, name=t.name, manager=t.manager)
    return render_template("student-edit.html", form=form)

@app.route('/studenti/')
def students():
    students_list = StudentManager.get_all()
    return render_template("students-list.html", students = students_list)



@app.route("/prace-nova/", methods = ["GET", "POST"])
def project_add():
    form = ProjectForm()
    if request.method == "POST":
        if form.validate():
            """
            t = TeacherManager.create_teacher(login=form.data.get("login"),
                                              name=form.data.get("name"),
                                              manager=form.data.get("manager"))
            """
            flash(f"Úspěšně přidána práce {form.data.get('name')}")
            return redirect(url_for("project_add"))
        else:
            flash("Chyba při přidání práce!")
    return render_template("project-add.html", form=form)

@app.route('/prace-seznam/')
def projects():
    projects_list = ProjectManager.get_all()
    return render_template("projects-list.html", projects = projects_list)


if __name__ == '__main__':
    app.run()
