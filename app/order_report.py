from datetime import datetime
from .serializer import OrderSchema, Order,PeriodSchema

from flask import Blueprint, jsonify, request, current_app
from .vehicles import *
from .period import *


# Blueprint init
bp_order_report = Blueprint('order_report', __name__)

@bp_order_report.route('/report', methods=['GET'])
def get_order():
    """
    Get all order in the database.
    """
    date = request.json.get('date')

    order_schema = OrderSchema(many=True)
    order = Order.query.filter(Order.order_date == date)

    return order_schema.jsonify(order), 200
