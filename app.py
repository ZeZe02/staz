from flask import Flask, render_template, request, flash, redirect, url_for
from pony.flask import Pony
from models import *


app = Flask(__name__)
app.secret_key = "safafafaijwdugwzrhofbweuhfkbewbowfv"
Pony(app)



@app.route('/')
def hello_world():
    return render_template("index.html", pozdrav="Ahoj", cisla=range(0,10), zobraz=True)

@app.route("/ucitel/", methods=["GET","POST"])
def teacher():
    if request.method == "POST":
        fname = request.form.get("fname", "")
        lname = request.form.get("lname", "")
        fullname = f"{fname} {lname}"
        login = request.form.get("login", "")
        manager = request.form.get("manager", "")
        create_teacher(fullname, login, manager)
        flash("Vytvořeno!!")
        return redirect(url_for("teacher"))
    else:
        return render_template("teacher.html")


@app.route("/ucitele/")
def pozdrav_ucitel():
    return render_template("ucitele.html")

@app.route('/ucitele/<name>/')
def krasny_den(name):
    return 'Krásný den ' + str(name)


if __name__ == '__main__':
    app.run()
