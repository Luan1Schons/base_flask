from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token
from app.models.user import User, Token
from app import db


def auth_user(email, password):
    # Verificar se o usuário existe
    user = User.query.filter_by(email=email, password=password).first()
    expires = timedelta(hours=1)

    if user:
        # Obter o token anterior, se existir
        previous_token = Token.query.filter_by(user_id=user.id).first()
        if previous_token:
            current_timestamp = datetime.timestamp(datetime.utcnow())
            if previous_token.expires_timestamp > current_timestamp:
                # O timestamp do token anterior ainda não terminou, retornar erro
                return previous_token.token, previous_token.expires_timestamp, None

            # Excluir o token anterior
            db.session.delete(previous_token)
            db.session.commit()

        # Criação do novo token com a duração definida
        access_token = create_access_token(identity=user.id, expires_delta=expires)

        # Salvar o novo token na tabela 'tokens'
        token = Token(token=access_token, user_id=user.id)
        db.session.add(token)
        db.session.commit()

        return access_token, token.expires_timestamp, None
    return False, None, "Usuário não encontrado"


def regen_token(user_id):
    # Verificar se o usuário existe
    user = User.query.filter_by(id=user_id).first()
    expires = timedelta(hours=1)

    if user:
        # Obter o token anterior, se existir
        previous_token = Token.query.filter_by(user_id=user.id).first()
        if previous_token:
            current_timestamp = datetime.timestamp(datetime.utcnow())
            if previous_token.expires_timestamp > current_timestamp:
                # O timestamp do token anterior ainda não terminou, retornar erro
                return previous_token.token, previous_token.expires_timestamp, None

            # Excluir o token anterior
            db.session.delete(previous_token)
            db.session.commit()

        # Criação do novo token com a duração definida
        access_token = create_access_token(identity=user.id, expires_delta=expires)

        # Salvar o novo token na tabela 'tokens'
        token = Token(token=access_token, user_id=user.id)
        db.session.add(token)
        db.session.commit()

        return access_token, token.expires_timestamp, None
    return False, None, "Usuário não encontrado"


def logout_user(user_id):
    previous_token = Token.query.filter_by(user_id=user_id).first()
    if previous_token:
        db.session.delete(previous_token)
        db.session.commit()

    return True
