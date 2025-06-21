from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/health')
def health():
    return jsonify({"status": "ok"})

@api.route('/drones', methods=['GET'])
def list_drones():
    return jsonify({"drones": []})  # Placeholder

@api.route('/drones', methods=['POST'])
def add_drone():
    data = request.json
    return jsonify({"message": "Drone added", "data": data})

