from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from app import db

 

class GameStatusEnum(db.Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"

   
class User(db.Model):
    user_id = db.Column(db.String(240), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    upadted_at = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(240), nullable=False)
    avatar = db.Column(db.String(240), nullable=False)
    about = db.Column(db.String(240), nullable=False)
    banner = db.Column(db.String(240), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
    
class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(240), db.ForeignKey('user.user_id'), nullable=False)
    oppenent_id = db.Column(db.String(240), db.ForeignKey('user.user_id'), nullable=False)
    game_status = db.Column(db.Enum(GameStatusEnum), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return '<Game %r>' % self.game_id