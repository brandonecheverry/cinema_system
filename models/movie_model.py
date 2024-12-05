from config import db

class MovieModel:
    @staticmethod
    def create_movie(movie_data):
        return db.movies.insert_one(movie_data)

    @staticmethod
    def update_movie_availability(movie_id, availability):
        return db.movies.update_one({"_id": movie_id}, {"$set": {"availability": availability}})
