from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

active_users = set()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Function to send notifications to all active users
def send_notification(notification):
    socketio.emit('notification', notification, broadcast=True)

@socketio.on('connect')
def test_connect():
    print('Client connected')
    active_users.add(request.sid)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    active_users.remove(request.sid)

if __name__ == '__main__':
    socketio.run(app)
