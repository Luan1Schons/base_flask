from sqlalchemy.exc import SQLAlchemyError
from flask_restful import marshal, fields
from app import db
from app.models.user import User
from app.helpers.utils import Utils

def create_user(username, email, password):
    user = User(username=username, email=email, password=password)

    try:
        db.session.add(user)
        db.session.commit()
        return True, None
    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = Utils.get_error_message(e)
        return False, error_message


def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        return user_data
    else:
        return None


def update_user(user_id, username, email):
    user = User.query.get(user_id)

    if user is None:
        return False, "Usuário não encontrado."

    # Verificar se outro usuário já possui o mesmo username ou email
    if User.query.filter(
        User.id != user_id, (User.username == username) | (User.email == email)
    ).first():
        return False, "Porfavor escolha um username ou email diferente."

    # Atualizar os dados do usuário
    user.username = username
    user.email = email

    try:
        db.session.commit()
        return True, None
    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = Utils.get_error_message(e)
        return False, error_message


def delete_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        return False, "Usuário não encontrado."

    try:
        db.session.delete(user)
        db.session.commit()
        return True, None
    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = Utils.get_error_message(e)
        return False, error_message


def users_list(page, per_page, sort_by, sort_order):
    try:
        # Defina a ordenação com base nos parâmetros recebidos
        sort_column = (
            getattr(User, sort_by) if hasattr(User, sort_by) else User.username
        )
        sort_direction = getattr(sort_column, sort_order.lower(), "asc")

        users_query = User.query.order_by(sort_direction()).paginate(
            page=page, per_page=per_page
        )
        total_users = users_query.total
        users = users_query.items

        if users:
            user_fields = {
                "id": fields.Integer,
                "username": fields.String,
                "email": fields.String,
            }

            serialized_users = [marshal(user, user_fields) for user in users]
            return serialized_users, total_users, None
        return None, 0, "Nenhum usuário encontrado"
    except Exception as e:
        error_message = Utils.get_error_message(e)
        return None, 0, error_message
