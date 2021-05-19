from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

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


if __name__ == '__main__':
    app.run()
