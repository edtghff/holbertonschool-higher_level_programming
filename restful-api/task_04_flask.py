from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
    }

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return 'Not found'
    
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not all(key in data for key in ['username', 'name', 'age', 'city']):
        return jsonify({"error": "Missing requiring fields"}), 400

    users[data['username']] = {
        'name': data['name'],
        'age': data['age'],
        'city': data['city']
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[data['username']]
    }), 201

if __name__ == "__main__":
    app.run()