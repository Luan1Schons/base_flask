from datetime import datetime
from app import db
from app.models.user import User

class UserStatus(db.Model):
    __tablename__ = "users_status"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship("User", backref="status", lazy="dynamic")

    def __init__(self, description):
        self.description = description