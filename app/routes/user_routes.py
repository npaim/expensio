from flask import Blueprint, request, jsonify
from app.services.user_service import add_user, get_users

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/add', methods=['POST'])
def add_user_route():
    data = request.get_json()
    user = add_user(data)
    return jsonify(user), 201

@user_routes.route('/all', methods=['GET'])
def get_all_users():
    users = get_users()
    return jsonify(users), 200
