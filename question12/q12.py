from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Function to update data every few seconds
def update_data():
    import time
    while True:
        socketio.emit('update', {'data': 'New data to be displayed'})
        time.sleep(5)

@socketio.on('connect')
def test_connect():
    print('Client connected')
    # Start a background task to update data periodically
    socketio.start_background_task(target=update_data)

if __name__ == '__main__':
    socketio.run(app)
