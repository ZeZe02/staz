from livereload import Server
from . import app

app.debug = True
server = Server(app.wsgi_app)
# app.run(debug=True)
server.serve()
