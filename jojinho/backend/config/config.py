# exemplo mínimo
# derivado de: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

# importações
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# configurações
app = Flask(__name__) # vínculo com o Flask

# aplica o CORS
CORS(app)

# sqlalchemy
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'teste.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings

db = SQLAlchemy(app) # vínculo com o SQLAlchemy

# para exibir versões das bibliotecas:
# pip3 freeze
# para instalar requisitos:
# pip3 install flask
# pip3 install flask_sqlalchemy

# referência oficial:
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

class Tableimg(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome_foto = db.Column(db.Text)

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, primary_key=False)
    pintos = db.Column(db.Integer, primary_key=False)


# comando mágico necessário a partir do python 10
app.app_context().push()
