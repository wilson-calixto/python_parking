from flask import Blueprint
from ..controllers.order import *


# Blueprint init
bp_order = Blueprint('order', __name__)

@bp_order.route('/order', methods=['GET'])
def call_get_order():
    return get_order()
    
@bp_order.route('/init_order', methods=['POST'])
def call_init_order():
    return init_order()

@bp_order.route('/finish_order', methods=['POST'])
def call_finish_order():
    return finish_order()