from imaplib import Response_code

from flask import Flask, render_template, request, flash, redirect, url_for, Response
from pony.flask import Pony
from pony.orm import commit, db_session, select

import models
from forms import TeacherForm
from managers import TeacherManager

app = Flask(__name__)
app.secret_key = "safafafaijwdugwzrhofbweuhfkbewbowfv"
Pony(app)


@app.route('/')
def homepage():
    return render_template('pages/homepage/index.html')


@app.route('/ajax-test/', methods=['POST'])
def ajax_test():
    response = Response()
    response.set_data('')
    response.status=500
    return response


@app.route('/pridat-ucitel/', methods=['GET', 'POST'])
def teacher():
    t = TeacherManager.get_teacher(1)
    form = TeacherForm()

    if request.method == 'POST':
        if form.validate():
            t = TeacherManager.create_teacher(**form.data)
            flash('Vytvořeno !!')
            return redirect(url_for('teacher'))
        else:
            flash('Nevytvořeno')

    return render_template('pages/pridat-ucitele/teacher.html', form=form)


@app.route('/ucitele/')
def teachers():
    list_of_teachers = TeacherManager.get_all_teachers()
    return render_template('pages/ucitele/list_of_teachers.html',
                           teachers=list_of_teachers)


if __name__ == '__main__':
    app.run()
