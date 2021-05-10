import socket

from flask import Flask

from flask import render_template, redirect


app = Flask(__name__)

@app.route("/")

def home():
    Hname = socket.gethostname()
    return Hname

@app.route("/index1/")
def ind():
    return redirect("https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y2Fyc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80")
                

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
