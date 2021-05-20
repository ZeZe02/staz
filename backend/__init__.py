from flask import Flask
from pony.flask import Pony

app = Flask(__name__)
pony = Pony(app)

from . import models
from . import routes
