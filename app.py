from flask import Flask, render_template, request, flash, redirect, url_for
from pony.flask import Pony
from models import *

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
        teacher = create_teacher(fullname, login, manager)
        flash("Vytvořeno!")
        return redirect(url_for("teacher"))
    return render_template("teacher.html",msg=msg)


@app.route('/ucitele/<name>/')
def hello_teachers(name):
    return f'Hello Teacher {name}!'

if __name__ == '__main__':
    app.run()
