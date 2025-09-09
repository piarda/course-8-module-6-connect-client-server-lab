from flask import Flask, jsonify, request
from flask_cors import CORS
from data import events, add_event

app = Flask(__name__)
CORS(app, origins=["http://localhost:8000"])

@app.route('/')
def home():
    # Return JSON welcome message
    return jsonify({"message": "Welcome to the Events Catalog API"})

@app.route('/events', methods=['GET'])
def get_events():
    # Return list of events as JSON
    return jsonify(events)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()

    # Validate incoming JSON has 'title'
    if not data or 'title' not in data:
        return jsonify({"error": "Missing 'title' in request data"}), 400

    # Use add_event helper function from data.py
    new_event = add_event({
        "title": data['title']
    })

    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)
