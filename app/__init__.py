from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from configs import config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    # Cria uma instância do aplicativo Flask
    app = Flask(__name__)

    # Configuração do cors
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Carrega as configurações do arquivo configs.py
    app.config.from_object(config['development'])

    # Inicializa o JWT
    from app.helpers.jwt import jwt
    jwt.init_app(app)

    # Configura a extensão SQLAlchemy para usar o aplicativo Flask
    db.init_app(app)
    migrate = Migrate(app, db)

    from app import api
    app.register_blueprint(api.routes)

    return app
