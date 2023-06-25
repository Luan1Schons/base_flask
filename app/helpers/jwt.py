from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from app.models.user import User

app = Flask(__name__)
jwt = JWTManager(app)



