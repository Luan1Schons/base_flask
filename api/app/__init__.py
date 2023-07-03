from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from configs import config

db = SQLAlchemy()


def create_app():
    # Cria uma instância do aplicativo Flask
    app = Flask(__name__)

    # Carrega as configurações do arquivo configs.py
    app.config.from_object(config["development"])

    # Configura o CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Inicializa o JWT
    from app.helpers.jwt import jwt

    jwt.init_app(app)

    # Configura a extensão SQLAlchemy para usar o aplicativo Flask
    db.init_app(app)
    Migrate(app, db)

    from app import api

    app.register_blueprint(api.routes)

    return app
