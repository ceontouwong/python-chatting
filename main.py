from flask import Flask, request, render_template, flash
from flask_socketio import SocketIO
import time
app = Flask(__name__)
async_mode = None
app.config['SECRET_KEY'] = "TestForFirstTime"
socketio = SocketIO(app)

@app.route('/', methods = ['GET', 'POST'])
def chatbox():
    Talkto = "Yuki"
    return render_template('chatbox.html', name = Talkto)

@socketio.on('connect')
def Test_Connect():
    print('CONNECTED!')
    socketio.emit('response', "CONNECTED TO SERVER SUCCESSFULLY!")
    running()

@socketio.on('send')
def resp_send(msg):
    socketio.emit('ReToSend', "I know that.")

def sendback(msg):
    socketio.emit('resp', msg)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

def dealWithMsg(msg):
    msg = "I have heard what you said:" + msg
    return msg

def running():
    for i in range(5):
        time.sleep(1)
        sendback("emmm...")

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
    running()
