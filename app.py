from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/ucitele/')
def hello_teacher():
    return render_template('ucitele.html')


@app.route('/ucitele/<name>/')
def hello_teacher_name(name):
    return "HI " + str(name)




if __name__ == '__main__':
    app.run()
