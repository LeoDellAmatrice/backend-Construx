from flask import Flask, request, jsonify
from flask_cors import CORS
# from database.login import login_views
app = Flask(__name__)
CORS(app)


@app.route('/api')
def index():
    return jsonify({'message': 'seja bem vindo ao site Construx.'})


if __name__ == '__main__':
    app.run(debug=True)