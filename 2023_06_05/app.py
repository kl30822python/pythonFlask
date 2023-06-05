from flask import Flask

app = Flask(__name__) #__name__是app的名字

@app.route("/")
def index():
    return "<h1>Hello! Kochung</h1>"