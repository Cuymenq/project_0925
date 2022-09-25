from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))
    token = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def hash_my_password(self, password):
        self.password = generate_password_hash(password)

    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(1200))
    type = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)