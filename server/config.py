from flask_sqlalchemy import SQLAlchemy
from app import app
import os
app.config['SECRET_KEY'] = '564se4r4sd5f48er454tr45sd8fer4'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or \
'mysql://root:rootroot@localhost/TicTacToe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
