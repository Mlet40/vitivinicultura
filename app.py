from flask import Flask, jsonify, request
from services.vinho_service import get_vinhos
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)


# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Dados de exemplo para cada endpoint
producao_data = [
    {"id": 1, "control": "control1", "produto": "produto1", "categoria": "categoria1", "ano": 2020},
    {"id": 2, "control": "control2", "produto": "produto2", "categoria": "categoria2", "ano": 2021}
]

processa_viniferas_data = [
    {"id": 1, "control": "control1", "cultivar": "cultivar1", "categoria": "categoria1", "ano": 2020},
    {"id": 2, "control": "control2", "cultivar": "cultivar2", "categoria": "categoria2", "ano": 2021}
]

comercio_data = [
    {"id": 1, "control": "control1", "produto": "produto1", "categoria": "categoria1", "ano": 2020},
    {"id": 2, "control": "control2", "produto": "produto2", "categoria": "categoria2", "ano": 2021}
]

importacao_vinhos_data = [
    {"id": 1, "país": "país1", "ano": 2020},
    {"id": 2, "país": "país2", "ano": 2021}
]

exportacao_vinhos_data = [
    {"id": 1, "país": "país1", "ano": 2020},
    {"id": 2, "país": "país2", "ano": 2021}
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vinhos')
def list_vinhos():
    vinhos = get_vinhos()
    return jsonify(vinhos)

@app.route('/producao', methods=['GET'])
@jwt_required()
def get_producao():
    return jsonify(producao_data), 200


@app.route('/processa-viniferas', methods=['GET'])
@jwt_required()
def get_processa_viniferas():
    return jsonify(processa_viniferas_data), 200


@app.route('/comercio', methods=['GET'])
@jwt_required()
def get_comercio():
    return jsonify(comercio_data), 200


@app.route('/importacao-vinhos', methods=['GET'])
@jwt_required()
def get_importacao_vinhos():
    return jsonify(importacao_vinhos_data), 200


@app.route('/exportacao-vinhos', methods=['GET'])
@jwt_required()
def get_exportacao_vinhos():
    return jsonify(exportacao_vinhos_data), 200


# Endpoint para gerar token JWT para testes
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity={'username': username})
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    app.run(debug=True)
