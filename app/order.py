from .serializer import OrderSchema, Teste_orderSchema,PeriodSchema

from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_order = Blueprint('order', __name__)

@bp_order.route('/order', methods=['GET'])
def get_order():
    """
    Get all order in the database.
    """

    order_schema = OrderSchema(many=True)
    order = Order.query.all()
    return order_schema.jsonify(order), 200

@bp_order.route('/order', methods=['POST'])
def add_order():
    """
    Add order in database.
    """
    # order_schema = Teste_orderSchema()
    order_schema = OrderSchema()
    order = order_schema.load(request.json)
    current_app.db.session.add(order)
    current_app.db.session.commit()
    return order_schema.jsonify(order), 201

