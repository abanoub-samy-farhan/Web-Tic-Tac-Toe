from flask import request, jsonify, url_for
from flask_login import login_required, current_user
from .models import Game, GameStatusEnum, RoomState, User, Base
from .extensions import db
from app import socketio, app
from flask_socketio import send, emit, join_room, leave_room
from flask import g
# import easyAI
import uuid


class TicTacToeGame():
    def __init__(self, user_id, opponent_id):
        self.user_id = user_id
        self.opponent_id = opponent_id
        self.board = [' ' for _ in range(9)]
        self.game = Game(user_id=user_id, opponent_id=opponent_id, game_status=GameStatusEnum.IN_PROGRESS.value)
        db.session.add(self.game)
        db.session.commit()


    def get_user(self):
        return User.query.get(self.user_id)
    
    def set_user(self, user):
        self.user_id = user.id

    def get_opponent(self):
        return User.query.get(self.opponent_id)
    
    def set_opponent(self, opponent):
        self.opponent_id = opponent.id

    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
    
    def get_game(self):
        return self.game
    
    def set_game(self, game):
        self.game = game
    

    def make_move(self, move, player):
        if self.board[move] == ' ':
            self.board[move] = player
            db.session.commit()
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'tie'
        return None


@app.route('/generate-invite', methods=['POST'])
@login_required
@socketio.on('generate_invite')
def generate_invite():

    game = Game(user_id=str(current_user.id), room_status=RoomState.WAITING)
    db.session.add(game)
    db.session.commit()

    invite_link = url_for('join_game', game_id=str(game.id), _external=True)

    socketio.emit('on_join', {'game_id': game.id})

    # g.gameBoard = TicTacToeGame()

    return jsonify({'invite_link': invite_link})


@app.route('/join-game/<string:game_id>', methods=['POST'])
@login_required
def join_game(game_id):
    game = Game.query.get_or_404(game_id)

    if game.room_status != RoomState.WAITING:
        return jsonify({'error': 'Game is not available for joining'}), 400

    if game.user_id == current_user.id:
        return jsonify({'error': 'You cannot join your own game'}), 400

    if game.opponent_id:
        return jsonify({'error': 'Game is full'}), 400

    game.opponent_id = str(current_user.id)
    game.room_status = RoomState.PLAAYING
    db.session.commit()

    socketio.emit('on_join', {'game_id': game.id})
    socketio.emit('start_game', {'game_id': game_id}, room=str(game_id))

    return jsonify({'message': 'Joined the game successfully', 'game_id': game.id})


@socketio.on('on_join')
def on_join(data):
    print("*****", data.get('game_id'))
    game_id = data.get('game_id')
    room = str(game_id)
    join_room(room)

@socketio.on('leave')
def on_leave(data):
    print("*****", data.get('game_id'))
    game_id = data.get('game_id')
    room = str(game_id)
    leave_room(room)

@socketio.on('start_game')
def start_game(data):
    game_id = data.get('game_id')
    room = str(game_id)
    print(">>>>> a player has joined.", room)
