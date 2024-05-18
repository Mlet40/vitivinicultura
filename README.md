# mle40-embrapa-vinho

API de dados de informações vinicultura da Embrapa
Descrição
A API de dados de informações vinicultura da Embrapa é projetada para gerenciar e fornecer informações sobre a produção, processamento, comércio, importação e exportação de vinhos. Esta API é utilizada para alimentar uma base de dados que será usada para treinar modelos de machine learning, visando otimizar e prever diferentes aspectos da indústria vinícola.

# Funcionalidades
Obter informações sobre a produção de vinhos.
Obter informações sobre o processamento de viniferas.
Obter informações sobre o comércio de vinhos.
Obter informações sobre a importação de vinhos.
Obter informações sobre a exportação de vinhos.
Autenticar usuários e fornecer tokens JWT para acesso seguro.

# Tecnologias Utilizadas
Python
Flask
Flask-JWT-Extended
OpenAPI/Swagger
Configuração e Execução
Pré-requisitos
Python 3.8 ou superior
Pip (gerenciador de pacotes do Python)

# Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu_usuario/vinhos_api.git

cd vinhos_api
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt

Configuração do JWT
Abra o arquivo app.py e configure a chave secreta para o JWT:
python
Copiar código
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'
Executando a API
Inicie a aplicação:

bash
Copiar código
flask run
Acesse a API no navegador ou use uma ferramenta como curl ou Postman para fazer requisições:

arduino
Copiar código
http://localhost:5000
Endpoints
Login

POST /login: Autentica o usuário e retorna um token JWT.
Requisição:
json
Copiar código
{
  "username": "test",
  "password": "test"
}
Resposta:
json
Copiar código
{
  "access_token": "seu_token_jwt"
}
Producao

GET /producao: Obter todas as informações de produção de vinhos.
Requisição:
http
Copiar código
GET /producao HTTP/1.1
Host: localhost:5000
Authorization: Bearer seu_token_jwt
Processa Viniferas

GET /processa-viniferas: Obter todas as informações de processamento de viniferas.
Requisição:
http
Copiar código
GET /processa-viniferas HTTP/1.1
Host: localhost:5000
Authorization: Bearer seu_token_jwt
Comercio

GET /comercio: Obter todas as informações de comércio de vinhos.
Requisição:
http
Copiar código
GET /comercio HTTP/1.1
Host: localhost:5000
Authorization: Bearer seu_token_jwt
Importacao Vinhos

GET /importacao-vinhos: Obter todas as informações de importação de vinhos.
Requisição:
http
Copiar código
GET /importacao-vinhos HTTP/1.1
Host: localhost:5000
Authorization: Bearer seu_token_jwt
Exportacao Vinhos

GET /exportacao-vinhos: Obter todas as informações de exportação de vinhos.
Requisição:
http
Copiar código
GET /exportacao-vinhos HTTP/1.1
Host: localhost:5000
Authorization: Bearer seu_token_jwt
Alimentação da Base de Machine Learning
Os dados fornecidos por esta API podem ser utilizados para alimentar uma base de machine learning, permitindo a criação de modelos preditivos e análises avançadas na área de viticultura. A API foi desenhada para fornecer dados estruturados e facilmente integráveis em pipelines de dados para treinamento de modelos.

Contribuindo
Se você deseja contribuir com a API de Vinhos, por favor, siga estas diretrizes:

Fork o repositório.
Crie um branch para sua feature (git checkout -b minha-feature).
Commit suas mudanças (git commit -am 'Adiciona minha feature').
Push para o branch (git push origin minha-feature).
Crie um novo Pull Request.
