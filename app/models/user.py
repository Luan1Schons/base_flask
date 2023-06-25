from app import db
from datetime import datetime, timedelta

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    tokens = db.relationship('Token', backref='user', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Token(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), unique=True)
    expires_at = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(hours=1))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    @property
    def expires_formatted(self):
        return self.expires_at.strftime('%d/%m/%Y %H:%M:%S')
    
    @property
    def expires_timestamp(self):
        return int(self.expires_at.timestamp())
