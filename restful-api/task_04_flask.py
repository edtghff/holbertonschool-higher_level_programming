from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    
    if not data or not data.get('username'):
        return jsonify({'error': 'Username is required'}), 400

    username = data['username']

    if username in users:
        return jsonify({'error': 'Username already exists'}), 400

    user = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    
    users[username] = user
    
    return jsonify({'message': 'User added', 'user': user}), 201

@app.route('/users/<username>')
def get_user(username):
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])

@app.route('/status')
def status():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
