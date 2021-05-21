from flask import Flask, render_template, request, flash, redirect, url_for
from pony.flask import Pony
from pony.orm import commit, db_session, select

import models
from managers import TeacherManager

app = Flask(__name__)
app.secret_key = "safafafaijwdugwzrhofbweuhfkbewbowfv"
Pony(app)



@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/ucitel/', methods=['GET', 'POST'])
def teacher(login=None):
    msg = ""
    if request.method == 'POST':
        login = request.form.get('login', '')
        fname = request.form.get('fname', '')
        lname = request.form.get('lname', '')
        name = f'{fname} {lname}'
        manager = request.form.get("manager", '')
        teacher = models.create_teacher(fname=fname, lname=lname, login=login, manager=manager)
        flash("Vytvořeno!")
        return redirect(url_for("teacher"))
    else:
        return  render_template('teacher.html')



@app.route('/ucitele/')
def teachers():
    list_of_teachers = TeacherManager.get_teachers()

    return render_template("list_of_teachers.html", teachers = list_of_teachers)




@app.route('/grades/', methods=['GET', 'POST'])
def grade(name, order, grade):
    msg = ""
    if request.method == 'POST':
        fname = request.form.get('fname', '')
        lname = request.form.get('lname', '')
        name = request.form.get(f'{fname} {lname}', '')


if __name__ == '__main__':
    app.run()
