from flask import Flask, render_template
from pony.flask import Pony
import models

from livereload import Server

db = models.db

app = Flask(__name__)
pony = Pony(app)


@app.route("/")
def index():
    return render_template("base.html")


@app.get("/marek/")
def marek():
    return render_template("base.html")


@app.post("/marek/")
def marek_post():
    return render_template("base.html")


if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    # app.run(debug=True)
    server.serve()
