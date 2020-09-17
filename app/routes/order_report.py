from flask import Blueprint
from ..controllers.order_report import *


# Blueprint init
bp_order_report = Blueprint('order_report', __name__)

@bp_order_report.route('/report', methods=['GET'])
def call_get_orders_group_by_day():
    return get_orders_group_by_day()
    