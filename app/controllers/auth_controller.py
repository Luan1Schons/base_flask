from app.models.user import User, Token
from app import db
from flask_jwt_extended import create_access_token
from datetime import timedelta

def auth_user(email, password):
    # Verificar se o usuário existe
    user = User.query.filter_by(email=email, password=password).first()
    expires = timedelta(hours=1)

    if user:
        # Excluir o token anterior, se existir
        previous_token = Token.query.filter_by(user_id=user.id).first()
        if previous_token:
            db.session.delete(previous_token)
            db.session.commit()
            
        # Criação do token com a duração definida
        access_token = create_access_token(identity=user.id, expires_delta=expires)
        
        # Salvar o token na tabela 'tokens'
        token = Token(token=access_token, user_id=user.id)
        db.session.add(token)
        db.session.commit()

        return access_token, token.expires_timestamp, None
    else:
        return False, None,'Usuário não encontrado'

def logout_user(user_id):
    previous_token = Token.query.filter_by(user_id=user_id).first()
    if previous_token:
        db.session.delete(previous_token)
        db.session.commit()

    return True