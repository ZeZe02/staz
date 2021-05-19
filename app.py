from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.get("/marek/")
def marek():
    return render_template("base.html")


@app.post("/marek/")
def marek_post():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
