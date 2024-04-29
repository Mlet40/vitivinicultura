from flask import Flask, jsonify
from services.vinho_service import get_vinhos

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vinhos')
def list_vinhos():
    vinhos = get_vinhos()
    return jsonify(vinhos)

if __name__ == '__main__':
    app.run(debug=True)