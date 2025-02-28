from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

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
        return jsonify({
            "username": username,
            **users[username]
        })
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    if not all(key in data for key in ['username', 'name', 'age', 'city']):
        return jsonify({"error": "Missing required fields"}), 400

    if data['username'] in users:
        return jsonify({"error": "Username already exists"}), 400
    
    users[data['username']] = {
        'name': data['name'],
        'age': data['age'],
        'city': data['city']
    }

    return jsonify({
        "message": "User added",
        "user": users[data['username']]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)