from .serializer import OrderSchema, Teste_orderSchema,PeriodSchema

from flask import Blueprint, jsonify, request, current_app
from .vehicles import *
from .period import *


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
    
    temp ={   "fk_vehicle":"q",
        "fk_period":"q",
        "initial_hour":"q",
        "final_hour":"q",
        "hour_quantity":"q",
        "total_value":"q",
        "order_date":"q"
    }

    # request.json
    order = order_schema.load(temp)
    current_app.db.session.add(order)
    current_app.db.session.commit()
    
    vehicle=get_vehicle_by_license_plate_from_db(request.json.get('vehicle_license_plate'))

    # print("\n\n\n vehicle \n\n",(vehicle.vehicle_id))

    first_period = get_period_from_db(hour=9,day=1)
    
    print("\n\n\n first_period \n\n",(first_period))


    return order_schema.jsonify(order), 201
    # return 
