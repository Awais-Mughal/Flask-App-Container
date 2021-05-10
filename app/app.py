import socket

from flask import Flask

from flask import render_template, redirect


app = Flask(__name__)

@app.route("/")

def home():
    Hname = socket.gethostname()
    return ('Hostname is: ' + Hname)

@app.route("/index1/")
def ind1():
    Hname = socket.gethostname()
    image = 'pic/r.jpg'
    return render_template('index.html', hostname = Hname, pic = image )


@app.route("/index2/")
def ind2():
    Hname = socket.gethostname()
    image = 'pic/s.jpg'
    return render_template('index.html', hostname = Hname, pic = image )


@app.route("/index3/")
def ind3():
    return redirect("https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y2Fyc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80")
                

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
