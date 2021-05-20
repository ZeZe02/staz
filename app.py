from flask import Flask, render_template, request, flash, redirect, url_for
from pony.flask import Pony
import models

app = Flask(__name__)
app.secret_key = "safafafaijwdugwzrhofbweuhfkbewbowfv"
Pony(app)



@app.route('/')
def hello_world():
    return render_template("index.html", pozdrav="Ahoj", cisla = range(0,9), zobraz = True)

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
def hello_teacher():
    return render_template("ucitele.html")

@app.route('/ucitele/<name>')
def hello_teacher_name(name):
    return f"Yellow teacher {name}!"



if __name__ == '__main__':
    app.run()
