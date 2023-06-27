from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from app.helpers.json import Json
from app.controllers.user_controller import (
    create_user,
    get_user,
    update_user,
    delete_user,
    users_list,
)
from app.helpers.jwt import validate_token

# Cria um objeto Blueprint para usuários
users_bp = Blueprint("users", __name__)


@users_bp.route("/user", methods=["GET"])
@validate_token
def details_logged_user_route():
    # Obter dados da requisição
    current_user = get_jwt_identity()
    # Chamar a função de criação de usuário do controller
    user = get_user(current_user)
    # Verificar se o usuário foi encontrado
    if user:
        return Json.response(data=user, status_code=200)
    return Json.response(message="Usuario não encontrado.", status_code=404)


@users_bp.route("/users/list", methods=["GET"])
@validate_token
def list_users_route():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    sort_by = request.args.get("sort_by", default="username", type=str)
    sort_order = request.args.get("sort_order", default="asc", type=str)

    # Chamar a função de listagem de usuários do controller
    users, total_users, error_message = users_list(page, per_page, sort_by, sort_order)

    if users:
        last_page = int(total_users / per_page) + (total_users % per_page > 0)
        response_data = {
            "list": users,
            "total_users": total_users,
            "current_page": page,
            "next_page": page + 1 if page < last_page else None,
            "last_page": last_page,
        }
        return Json.response(data=response_data, status_code=200)
    return Json.response(
        message="Erro ao listar usuários.", status_code=422, error=error_message
    )


@users_bp.route("/users", methods=["POST"])
@validate_token
def create_user_route():
    # Obter dados da requisição
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    # Chamar a função de criação de usuário do controller
    success, error_message = create_user(username, email, password)

    if success:
        return Json.response(message="Usuário criado com sucesso.", status_code=200)
    return Json.response(
        message="Erro ao criar usuário", status_code=422, error=error_message
    )


@users_bp.route("/users/<int:user_id>", methods=["GET"])
@validate_token
def get_user_route(user_id):
    user = get_user(user_id)

    # Verificar se o usuário foi encontrado
    if user:
        return Json.response(data=user, status_code=200)
    return Json.response(message="Usuario não encontrado.", status_code=404)


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
@validate_token
def update_user_route(user_id):
    # Obter dados da requisição
    username = request.json["username"]
    email = request.json["email"]

    # Chamar a função de atualização de usuário do controller
    success, error_message = update_user(user_id, username, email)

    if success:
        return Json.response(message="Usuário atualizado com sucesso.", status_code=200)
    return Json.response(
        message="Erro ao atualizar usuário", status_code=422, error=error_message
    )


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
@validate_token
def delete_user_route(user_id):
    # Chamar a função de exclusão de usuário do controller
    success, error_message = delete_user(user_id)

    if success:
        return Json.response(message="Usuário excluído com sucesso.", status_code=200)
    return Json.response(
        message="Erro ao excluir usuário", status_code=422, error=error_message
    )
