from flask import Blueprint
from app.routes.auth import auth_bp
from app.routes.users import users_bp

# Cria um objeto Blueprint para usuários
routes = Blueprint('auth', __name__)

# Registra os blueprints
routes.register_blueprint(auth_bp)
routes.register_blueprint(users_bp)