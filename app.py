from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Service 2!"
@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Service 2"})

@app.route('/ping')
def ping():
    return jsonify({"service": "2", "status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
