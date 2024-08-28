from .extensions import db
from enum import Enum
from datetime import datetime
import uuid

from flask_login import UserMixin

class GameStatusEnum(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"

class RoomState(Enum):
    WAITING = "waiting"
    PLAAYING = "playing"

class Base:
    id = db.Column(db.String(240), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model, Base, UserMixin):
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(240), nullable=False)
    avatar = db.Column(db.String(240), nullable=False)
    banner = db.Column(db.String(240), nullable=False)
    about = db.Column(db.String(240), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Game(db.Model, Base):
    user_id = db.Column(db.String(240), db.ForeignKey('user.id'), nullable=False)
    opponent_id = db.Column(db.String(240), db.ForeignKey('user.id'), nullable=True)
    game_status = db.Column(db.Enum(GameStatusEnum), nullable=True)
    room_status = db.Column(db.Enum(RoomState), nullable=False)
    def __repr__(self):
        return '<Game %r>' % self.game_id
