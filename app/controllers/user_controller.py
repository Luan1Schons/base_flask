from app.models.user import User
from app import db
from app.helpers.utils import Utils
from sqlalchemy.exc import SQLAlchemyError

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
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return user_data
    else:
        return None

def update_user(user_id, username, email):
    user = User.query.get(user_id)

    if user is None:
        return False, 'Usuário não encontrado.'

    # Verificar se outro usuário já possui o mesmo username ou email
    if User.query.filter(User.id != user_id, (User.username == username) | (User.email == email)).first():
        return False, 'Porfavor escolha um username ou email diferente.'

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
        return False, 'Usuário não encontrado.'

    try:
        db.session.delete(user)
        db.session.commit()
        return True, None
    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = Utils.get_error_message(e)
        return False, error_message
    
