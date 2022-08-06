from flask import Flask
app = Flask(__name__)

@app3.route('/')
def hello_world():
    return 'Hello Sammy!'