from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "Servidor de Chat funcionando 🚀"

@socketio.on("message")
def manejar_msg(msg):
    print("Mensaje recibido:", msg)
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
