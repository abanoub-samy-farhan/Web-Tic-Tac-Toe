from flask_socketio import SocketIO
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .extensions import db, login_manager
from .models import User
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") or \
'mysql://root:rootroot@localhost/TicTacToe'

# Initialize extensions
db.init_app(app)
login_manager.init_app(app)
socketio = SocketIO(app)

migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from app import models, views, tic_tac_toe
