from flask import Flask
from pony.flask import Pony
from flask_cors import CORS

app = Flask(__name__)
pony = Pony(app)
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:*"}})

from . import models
from . import routes
