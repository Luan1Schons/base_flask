from flask import Blueprint, jsonify, request
from app.helpers.json import Json
from app.controllers.user_controller import create_user, get_user, update_user, delete_user
from flask_jwt_extended import get_jwt_identity
from app.helpers.jwt import validate_token

# Cria um objeto Blueprint para usuários
users_bp = Blueprint('users', __name__)

@users_bp.route('/user', methods=['GET'])
@validate_token
def details_logged_user_route():
    # Obter dados da requisição
    current_user = get_jwt_identity()
    # Chamar a função de criação de usuário do controller
    user = get_user(current_user)
    
    # Verificar se o usuário foi encontrado
    if user:
        return Json.response(data=user, status_code=200)
    else:
        return Json.response(message='Usuario não encontrado.', status_code=404)

@users_bp.route('/users', methods=['POST'])
@validate_token
def create_user_route():
    # Obter dados da requisição
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    # Chamar a função de criação de usuário do controller
    success, error_message = create_user(username, email, password)

    if success:
        return Json.response(message='Usuário criado com sucesso.', status_code=200)
    else:
        return Json.response(message='Erro ao criar usuário', status_code=422, error=error_message)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
@validate_token
def get_user_route(user_id):

    user = get_user(user_id)
    
    # Verificar se o usuário foi encontrado
    if user:
        return Json.response(data=user, status_code=200)
    else:
        return Json.response(message='Usuario não encontrado.', status_code=404)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
@validate_token
def update_user_route(user_id):
    # Obter dados da requisição
    username = request.json['username']
    email = request.json['email']

    # Chamar a função de atualização de usuário do controller
    success, error_message = update_user(user_id, username, email)

    if success:
        return Json.response(message='Usuário atualizado com sucesso.', status_code=200)
    else:
        return Json.response(message='Erro ao atualizar usuário', status_code=422, error=error_message)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
@validate_token
def delete_user_route(user_id):
    # Chamar a função de exclusão de usuário do controller
    success, error_message = delete_user(user_id)

    if success:
        return Json.response(message='Usuário excluído com sucesso.', status_code=200)
    else:
        return Json.response(message='Erro ao excluir usuário', status_code=422, error=error_message)
