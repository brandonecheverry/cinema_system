from config import db

class PurchaseModel:
    @staticmethod
    def create_purchase(purchase_data):
        return db.purchases.insert_one(purchase_data)

    @staticmethod
    def find_purchases_by_user(user_id):
        return db.purchases.find({"user_id": user_id})
