from datetime import datetime
from .serializer import OrderSchema, Order,PeriodSchema

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

@bp_order.route('/init_order', methods=['POST'])
def add_order():
    """
    Add order in database.
    """
    # TODO adicionar tratamento de erro

    vehicle=get_vehicle_by_license_plate_from_db(request.json.get('vehicle_license_plate'))

    actual_hour = get_actual_hour()

    actual_day = get_actual_weekday()

    actual_date = get_actual_date()


    first_period = get_period_from_db(hour=actual_hour,day=actual_day)
    #  print("vehicle\n\n",vehicle)
    # print("first_period\n\n",first_period)


    temp ={
        "fk_vehicle":vehicle.vehicle_id,
        "fk_period":first_period.period_id,
        "initial_hour":actual_hour,
        "final_hour":0,
        "hour_quantity":0,
        "total_value":0,
        "order_date":actual_date
    }

    order_schema = OrderSchema()    
    order = order_schema.load(temp)
    current_app.db.session.add(order)
    current_app.db.session.commit()
    


    return order_schema.jsonify(order), 201
    # return 



@bp_order.route('/finish_order', methods=['POST'])
def finish_order():
    """
    Add order in database.
    """
    # TODO adicionar tratamento de erro

    vehicle=get_vehicle_by_license_plate_from_db(request.json.get('vehicle_license_plate'))

    actual_hour = get_actual_hour()

    actual_day = get_actual_weekday()

    actual_date = get_actual_date()


    first_period = get_period_from_db(hour=actual_hour,day=actual_day)
    #  print("vehicle\n\n",vehicle)
    # print("first_period\n\n",first_period)


    temp ={
        "fk_vehicle":vehicle.vehicle_id,
        "fk_period":first_period.period_id,
        "initial_hour":actual_hour,
        "final_hour":0,
        "hour_quantity":0,
        "total_value":0,
        "order_date":actual_date
    }

    order_schema = OrderSchema()    
    order = order_schema.load(temp)
    current_app.db.session.add(order)
    current_app.db.session.commit()
    


    return order_schema.jsonify(order), 201




#TODO mover para a biblioteca utils
def get_actual_hour():
    
    return datetime.now().hour * 100 + datetime.now().minute

def get_actual_weekday():
    return datetime.now().weekday()
    

def get_actual_date():
    return datetime.now().date()