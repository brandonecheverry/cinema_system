from flask import Blueprint, request, jsonify
from models.user_model import UserModel  # Corrección de la importación

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def register_user():
    user_data = request.json
    UserModel.create_user(user_data)
    return jsonify({"message": "Usuario registrado exitosamente"}), 201
