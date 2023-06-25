from flask import Blueprint, jsonify, request
from app.helpers.json import Json
from app.controllers.user_controller import create_user, get_user, update_user, delete_user
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

# Cria um objeto Blueprint para usuários
users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
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
@jwt_required()
def get_user_route(user_id):

    user = get_user(user_id)
    
    # Verificar se o usuário foi encontrado
    if user:
        return Json.response(data=user, status_code=200)
    else:
        return Json.response(message='Usuario não encontrado.', status_code=404)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
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
def delete_user_route(user_id):
    # Chamar a função de exclusão de usuário do controller
    success, error_message = delete_user(user_id)

    if success:
        return Json.response(message='Usuário excluído com sucesso.', status_code=200)
    else:
        return Json.response(message='Erro ao excluir usuário', status_code=422, error=error_message)
