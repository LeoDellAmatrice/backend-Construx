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
        return jsonify({'sucesso': False, 'mensagem': 'Dados Invalidos'})

    return jsonify({'sucesso': login_views.verificar_usuario_db(email, senha)})


@app.route('/api/produtos')
def api_produtos():
    return jsonify(produtos_views.get_produtos())


@app.route('/api/busca/produtos/')
def api_busca_proutos():

    busca_name = request.args.get('busca_name', None)

    if busca_name is None:
        return jsonify({'sucesso': False, 'mensagem': 'Dados Invalidos'})

    return jsonify(produtos_views.busca_produtos_by_name(busca_name))

@app.route('/api/categorias')
def api_categorias():
    return jsonify(categorias_views.get_categorias())


@app.route('/api/categorias/<int:categoria_id>')
def api_categoria_by_id(categoria_id):
    return categorias_views.get_categorias_by_id(categoria_id)


@app.route('/api/produtos/categorias/<int:categoria_id>')
def api_produtos_by_id_categoria(categoria_id):
    return produtos_views.get_produtos_by_id_categoria(categoria_id)


@app.route('/api/produtos/<int:id_produto>')
def api_produto_by_id(id_produto):
    return produtos_views.get_produto_by_id(id_produto)


@app.route('/api')
def index():
    return jsonify({'message': 'seja bem vindo ao site Construx.'})


if __name__ == '__main__':
    app.run(debug=True)
