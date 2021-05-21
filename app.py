
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
    return render_template('pages/homepage/index.html')


@app.route('/pridat-ucitel/', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        fname = request.form.get('fname', '')
        lname = request.form.get('lname', '')
        login = request.form.get('login', '')
        t = TeacherManager.create_teacher(fname, lname, login)
        flash('Vytvořeno !!')
        return redirect(url_for('teacher'))
    return render_template('pages/pridat-ucitele/teacher.html')


@app.route('/ucitele/')
def teachers():
    list_of_teachers = TeacherManager.get_all_teachers()
    return render_template('pages/ucitele/list_of_teachers.html',
                           teachers=list_of_teachers)


if __name__ == '__main__':
    app.run()
