from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ucitele')
def hello_teacher():
    return 'Hi World!'


if __name__ == '__main__':
    app.run()
