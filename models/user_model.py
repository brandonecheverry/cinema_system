from config import db

class UserModel:
    @staticmethod
    def create_user(user_data):
        return db.users.insert_one(user_data)

    @staticmethod
    def find_user_by_email(email):
        return db.users.find_one({"email": email})
