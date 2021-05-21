from flask import Flask, render_template, request, flash, redirect, url_for
from pony.flask import Pony

from models import *
from forms import TeacherForm

app = Flask(__name__)
app.secret_key = "safafafaijwdugwzrhofbweuhfkbewbowfv"
Pony(app)


@app.route('/')
def hello_world():
   return render_template("index.html", pozdrav="Ahoj", cisla=range(0,10), zobraz=True)


# @app.route("/ucitel/", methods=["GET","POST"])
# def teacher():
#     if request.method == "POST":
#         fname = request.form.get("fname", "")
#         lname = request.form.get("lname", "")
#         fullname = f"{fname} {lname}"
#         login = request.form.get("login", "")
#         manager = request.form.get("manager", "")
#         Teacher.create_teacher(fullname, login, manager)
#         flash("Vytvořeno!!")
#         return redirect(url_for("teacher"))
#     else:
#         return render_template("teacher.html")
@app.route('/ucitel/', methods=['GET', 'POST'])
def teacher():
    form = TeacherForm()
    if request.method == 'POST':
        if form.validate():
            fname = form.data.get("fname", "")
            lname = form.data.get("lname", "")
            fullname = f"{fname} {lname}"
            login = form.data.get("login", "")
            manager = form.data.get("manager", "")
            Teacher.create_teacher(fullname, login, manager)
            flash('Vytvořeno !!')
            return redirect(url_for('teacher'))
        else:
            flash('Nevytvořeno')

    return render_template('teacher.html', form=form)

@app.route("/znamka/", methods=["GET","POST"])
def type_grade():
    if request.method == "POST":
        name = request.form.get("name", "")
        order = request.form.get("order", 0)
        create_type_grade(name, order)
        flash("Vytvořeno!!")
        return redirect(url_for("type_grade"))
    else:
        return render_template("type_grade.html")

@app.route("/ucitele/")
def teachers():
    list_of_teachers = Teacher.get_teachers()
    return render_template("forms/list_of_teachers.html",teachers=list_of_teachers)



if __name__ == '__main__':
    app.run()
