from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify({"username": username, **user})
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    required_fields = {"username", "name", "age", "city"}
    if not required_fields.issubset(data.keys()):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({
        "message": "User added",
        "user": {"username": username, **users[username]}
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
