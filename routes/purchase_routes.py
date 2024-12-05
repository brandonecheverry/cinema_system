from flask import Blueprint, request, jsonify
from models.purchase_model import PurchaseModel  

purchase_bp = Blueprint('purchase_bp', __name__)

@purchase_bp.route('/purchases', methods=['POST'])
def make_purchase():
    purchase_data = request.json
    PurchaseModel.create_purchase(purchase_data)
    return jsonify({"message": "Compra realizada exitosamente"}), 201
