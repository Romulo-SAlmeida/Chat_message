import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def message(data):
    print('Message from server:', data)

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')
    while True:
        message = input('Enter message: ')
        sio.emit('message', message)