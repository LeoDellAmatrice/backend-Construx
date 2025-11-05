from flask import Flask, request, jsonify
from flask_cors import CORS
import database.produtos.produtos_views as produtos_views
import database.categorias_views.categorias_views as categorias_views
import database.login.login_views as login_views

app = Flask(__name__)
CORS(app)


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json(force=True)

    try:
        email = data['email']
        senha = data['senha']
    except KeyError:
        return jsonify({'successo': False, 'mensagem': 'Dados Invalidos'})

    return jsonify({'successo': login_views.verificar_usuario_db(email, senha)})


@app.route('/api/produtos')
def api_produtos():
    return jsonify(produtos_views.get_produtos())

@app.route('/api/categorias')
def api_categorias():
    return jsonify(categorias_views.get_categorias())

@app.route('/api')
def index():
    return jsonify({'message': 'seja bem vindo ao site Construx.'})


if __name__ == '__main__':
    app.run(debug=True)