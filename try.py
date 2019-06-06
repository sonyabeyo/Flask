from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sonya')
def hello():
    return "Helldfdsffsdfsdfsfso World!"

@app.route('/aharon')
def ddd():
    return "Hell on earth World!"

if __name__ == '__main__':
    app.run("192.168.1.19", "8080")