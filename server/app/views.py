from app import app, db
from flask import request, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Game
import uuid


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.hashed_password, password):
        login_user(user)
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    avatar = data.get("avatar")
    banner = data.get("banner")
    about = data.get("about")

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    new_user = User(
        id=str(uuid.uuid4()),
        username=username,
        hashed_password=hashed_password,
        avatar=avatar,
        banner=banner,
        about=about
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@app.route("/protected", methods=["GET"])
@login_required
def protected():
    return jsonify({"message": "This is a protected route"})

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"})

@app.route("/profile")
@login_required
def profile():
    user = User.query.get(current_user.id)

    return jsonify({
        "username": user.username,
        "avatar": user.avatar,
        "banner": user.banner,
        "about": user.about
    })

@app.route("/profile/<string:id>")
@login_required
def profile_id(id):
    user = User.query.get_or_404(id)

    return jsonify({
        "username": user.username,
        "avatar": user.avatar,
        "banner": user.banner,
        "about": user.about
    })

@app.route("/match_history")
@login_required
def match_history():
    user_id = current_user.id
    matches = Game.query.filter(
        (Game.user_id == user_id) | (Game.opponent_id == user_id)
    ).all()

    match_history = []
    for match in matches:
        match_history.append({
            'game_id': match.id,
            'opponent_id': user_id if match.user_id == user_id else match.opponent_id,
            'result': match.result,
            'date_played': match.date_played.strftime('%Y-%m-%d %H:%M:%S')
        })

    return jsonify({'match_history': match_history})
