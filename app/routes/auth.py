from flask import Blueprint, jsonify, request
from app.helpers.json import Json
from flask_jwt_extended import get_jwt_identity
from app.controllers.auth_controller import auth_user, logout_user
from app.controllers.user_controller import get_user
from app.helpers.jwt import validate_token

# Cria um objeto Blueprint para usuários
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def auth_route():
    # Obter dados da requisição
    email = request.json['email']
    password = request.json['password']

    token, expires, message = auth_user(email, password)

    if token:
        return Json.response(data={'token': token, 'expires': expires}, status_code=201)
    else:
        return Json.response(message=message, status_code=401)

@auth_bp.route('/auth/regenerate-token', methods=['POST'])
def regenerate_token_route():
    # Obter dados da requisição
    email = request.json['email']
    password = request.json['password']

    token, expires, message = auth_user(email, password)

    if token:
        return Json.response(data={'token': token, 'expires': expires}, status_code=201)
    else:
        return Json.response(message=message, status_code=401)

@auth_bp.route('/auth/logout', methods=['POST'])
@validate_token
def logout_route():
    current_user = get_jwt_identity()
    # Chamar a função de criação de usuário do controller
    user = get_user(current_user)

    if user:
        logout = logout_user(user['id'])
        return Json.response(message="Usuário deslogado.", status_code=200)
    else:
        return Json.response(message="Não foi possível efetuar o logout", status_code=401)
