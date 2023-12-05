from backend.config.config import *
from backend.rotas.rotas import *

# rota padrao


@app.route("/")
def inicio():

    return 'pontos'

# inserindo a aplicação em um contexto :-/


with app.app_context():

    app.run(debug=True, host="0.0.0.0")
