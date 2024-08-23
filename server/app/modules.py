from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Column
from app import app
from app import db

class User(db.Model):
    user_id = db.Column(db.String(240), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(240), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
    
class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(240), db.ForeignKey('user.user_id'), nullable=False)
    game_winner = db.Column(db.String(80), nullable=True)
    game_lose = db.Column(db.String(80), nullable=True)
    game_draw = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return '<Game %r>' % self.game_id