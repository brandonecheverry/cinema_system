from flask import Blueprint, request, jsonify
from models.movie_model import MovieModel  # Corrección de la importación

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/movies', methods=['POST'])
def add_movie():
    movie_data = request.json
    MovieModel.create_movie(movie_data)
    return jsonify({"message": "Película añadida exitosamente"}), 201
