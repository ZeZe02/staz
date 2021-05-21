from . import app
from flask import render_template, jsonify


@app.route("/")
def index():
    return render_template("base.html")


@app.get("/marek/")
def marek():
    return render_template("base.html")


@app.post("/marek/")
def marek_post():
    return render_template("base.html")


@app.get("/api/start.json")
def start():
    data = "ahoj,nazdar,cau".split(",")
    return jsonify(data=data)
