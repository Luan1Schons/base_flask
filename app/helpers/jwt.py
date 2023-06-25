from functools import wraps
from flask import Flask, jsonify,request
from flask_jwt_extended import JWTManager, jwt_required
from app.models.user import Token

app = Flask(__name__)
jwt = JWTManager(app)

def validate_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')  # Obtém o token Bearer do cabeçalho Authorization
        token = token.replace('Bearer ', '') if token else None  # Remove o prefixo 'Bearer ' do token, se estiver presente

        # Verificar se o token existe no banco de dados
        if not Token.query.filter_by(token=token).first():
            return jsonify(message='Token inválido'), 401

        return func(*args, **kwargs)

    return jwt_required()(wrapper)


