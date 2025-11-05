import flask 
from controle.emailControle import envioEmail

app = flask.Flask(__name__)

app.register_blueprint(envioEmail)

app.run(
         
)