from flask import Flask, request, render_template, flash, redirect, url_for
from flask_socketio import SocketIO
from chatbot.bot import *
import time

bot = Yuki()
app = Flask(__name__)
async_mode = None
app.config['SECRET_KEY'] = "TestForFirstTime"
socketio = SocketIO(app)

#首页
@app.route('/')
def index():
    return redirect(url_for(chatbox))

@app.route('/yukibot/')
def chatbox():
    Talkto = "Yuki"
    return render_template('chatbox.html', name = Talkto)

@socketio.on('connect')
def Test_Connect():
    print('CONNECTED!')
    socketio.emit('response', "CONNECTED TO SERVER SUCCESSFULLY!")

@socketio.on('send')
def resp_send(msg):
    response = bot.getResponse(msg)
    socketio.emit('resp', response)

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
