from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

clients = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    clients[request.sid] = None
    print(f"Client connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    del clients[request.sid]
    print(f"Client disconnected: {request.sid}")

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    for client_sid in clients.keys():
        if client_sid != request.sid:
            emit('message', message, room=client_sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)
