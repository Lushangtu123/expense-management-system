# Auth Service
from flask import Flask, request, jsonify
app = Flask(__name__)

users = {"admin": "password"}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 401

if __name__ == '__main__':
    app.run(port=5001, debug=True)
