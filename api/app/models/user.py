from datetime import datetime, timedelta
from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    status_id = db.Column(db.Integer, db.ForeignKey('users_status.id'), default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tokens = db.relationship("Token", backref="user", lazy="dynamic")

    def __init__(self, username, email, password, status_id = 1):
        from app.models.user_status import UserStatus
        self.username = username
        self.email = email
        self.password = password
        self.status_id = status_id
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), unique=True)
    expires_at = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(hours=1))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    @property
    def expires_formatted(self):
        return self.expires_at.strftime("%d/%m/%Y %H:%M:%S")

    @property
    def expires_timestamp(self):
        return int(self.expires_at.timestamp())
