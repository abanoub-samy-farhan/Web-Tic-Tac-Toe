from .extensions import db
from enum import Enum
from datetime import datetime

from flask_login import UserMixin

class GameStatusEnum(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"

class Base:
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model, Base, UserMixin):
    id = db.Column(db.String(240), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(240), nullable=False)
    avatar = db.Column(db.String(240), nullable=False)
    banner = db.Column(db.String(240), nullable=False)
    about = db.Column(db.String(240), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Game(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(240), db.ForeignKey('user.id'), nullable=False)
    oppenent_id = db.Column(db.String(240), db.ForeignKey('user.id'), nullable=False)
    game_status = db.Column(db.Enum(GameStatusEnum), nullable=False)
    def __repr__(self):
        return '<Game %r>' % self.game_id
