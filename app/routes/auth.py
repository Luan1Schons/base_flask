from flask import Blueprint, jsonify, request
from app.helpers.json import Json
from app.controllers.auth_controller import auth_user

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

    token, message = auth_user(email, password)

    if token:
        return Json.response(data={'token': token}, status_code=201)
    else:
        return Json.response(message=message, status_code=401)
