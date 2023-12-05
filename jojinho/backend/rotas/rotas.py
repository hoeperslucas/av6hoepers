from backend.config.config import *
from flask import send_file



@app.route("/incluir/<string:classe>", methods=['post'])
def insert(pontuacao, nome):
    with app.app_context():
        jogador = Jogador(pintos=pontuacao, name=nome)
        db.session.add(jogador)
        db.session.commit()


@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        # print("comecando")
        file_val = request.files['image']
        # print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagens/' + file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado": "ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado": "erro", "detalhes": str(e)})

    return r


@app.route("/incluir_imagem", methods=['post'])
def incluir_pessoa():
    dados = request.get_json(force=True)
    print(dados)
    try:
        nova = Tableimg(**dados)
        db.session.add(nova)
        db.session.commit()
        return jsonify({"resultado": "ok", "detalhes": "oi"})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})

@app.route('/apareceimg/<int:id_imagem>')
def get_image(id_imagem):

    g = db.session.get(Tableimg, id_imagem)

    caminho = os.path.dirname(os.path.abspath(__file__))
    completo = os.path.join(caminho, 'imagens/'+ g.photo)
    return send_file(completo, mimetype='image/gif')
