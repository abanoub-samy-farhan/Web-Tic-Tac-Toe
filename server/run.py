from app import app, socketio


if __name__ == '__main__':
    app.run(port=3000, debug=True)
    # socketio.run(app)
    