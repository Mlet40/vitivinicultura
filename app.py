from flask import Flask, jsonify, request, send_from_directory
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_swagger_ui import get_swaggerui_blueprint
from services.data_processing_service import DataProcessingService

app = Flask(__name__)
data_service = DataProcessingService()

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/comercio', methods=['GET'])
@jwt_required()
def comercio():
    df = data_service.get_comercio()
    return jsonify(df.to_dict(orient='records'))

@app.route('/exportacao', methods=['GET'])
@jwt_required()
def exportacao():
    df = data_service.get_exportacao()
    return jsonify(df.to_dict(orient='records'))

@app.route('/importacao', methods=['GET'])
@jwt_required()
def importacao():
    df = data_service.get_importacao()
    return jsonify(df.to_dict(orient='records'))

@app.route('/processa', methods=['GET'])
@jwt_required()
def processa():
    df = data_service.get_processa()
    return jsonify(df.to_dict(orient='records'))

@app.route('/producao', methods=['GET'])
@jwt_required()
def producao():
    df = data_service.get_producao()
    return jsonify(df.to_dict(orient='records'))

# Endpoint para gerar token JWT para testes
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity={'username': username})
    return jsonify(access_token=access_token), 200

# Configuração do Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Vinhos da Embrapa"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
