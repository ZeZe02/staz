from flask import Flask, render_template, request, url_for, redirect, flash
from pony.flask import Pony
from pony.orm import commit, db_session
#import models
from models import *

app = Flask(__name__)
app.secret_key = "asfuogasdhkjfbvasdhjkcbvdasjhk,56789"
Pony(app)



@db_session
@app.route('/')
def index():
    """
    u = Teacher(name="Igor",login="igor")
    commit()  # asi zde není potřeba, protože ten dekorátor db_session zajistí, že celá tato funkce bude brána jako jedna transakce a commitne se automaticky na konci funkce
    """
    jmeno = Teacher.get(id=1).name   # tohle ještě nezpůsobí SQL dotaz do DB, ale nachystá si to a až při použití té proměnné jmeno ten dotaz proběhne
    pracejednicky = Teacher.get(id=1).projects

    return render_template("index.html",jmeno=jmeno,pracejednicky=pracejednicky)

@app.route('/base/')
def muj_base():
    return render_template("base.html")
    return 'Hello World!'

#
@app.route('/ucitele/')
def ucitele():
    return render_template("ucitele.html")
    return 'Hello, teachers!'

# uvedu-li jmeno (nebo casteji spis id) ucitele, jdu do teto routy, jinak jdu do te horni
@app.route('/ucitele/<name>/')
def ucitele_name(name):
    return f'Hello, {name}!'




@app.route("/ucitel/", methods = ["GET", "POST"])
def ucitel():
    if request.method == "POST":
        login = request.form.get("login")
        jmeno = request.form.get("fname")
        prijm = request.form.get("lname")
        manager = request.form.get("manager")
        fullname = f"{jmeno} {prijm}"
        t = create_teacher(login=login, name=fullname, manager=manager)
        flash(f"Úspěšně přidán učitel {fullname} manager={manager}")  # nachystá do zásobníku (v rámci cookies) tuto "hlášku" a šablona base si ji pak použije
        # v ramci requestu se da detekovat i mobil - request z mobilniho telefonu
        # dat sem breakpoint a pak inspekovat request
        return redirect(url_for("ucitel"))
    return render_template("teacher.html")

if __name__ == '__main__':
    app.run()
