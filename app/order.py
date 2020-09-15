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

    vehicle = get_vehicle_by_license_plate_from_db(request.json.get('vehicle_license_plate'))
    # print('vehicle.vehicle_id',vehicle.vehicle_id)

    unfinshed_order = get_unfinshed_order_from_db_by_vehicle_id(vehicle.vehicle_id)
    # print('unfinshed_order',unfinshed_order)

    requires_a_new_order = update_order(unfinshed_order)

    # if(requires_a_new_order):
    #     insert_a_complemetary_order()


    # actual_hour = get_actual_hour()

    # actual_day = get_actual_weekday()

    # actual_date = get_actual_date()


    # first_period = get_period_from_db(hour=actual_hour,day=actual_day)
    # #  print("vehicle\n\n",vehicle)
    # # print("first_period\n\n",first_period)


    # temp ={
    #     "fk_vehicle":vehicle.vehicle_id,
    #     "fk_period":first_period.period_id,
    #     "initial_hour":actual_hour,
    #     "final_hour":0,
    #     "hour_quantity":0,
    #     "total_value":0,
    #     "order_date":actual_date
    # }

    # order_schema = OrderSchema()    
    # order = order_schema.load(temp)
    # current_app.db.session.add(order)
    # current_app.db.session.commit()
    


    # return order_schema.jsonify(order), 201
    return {"name":"em desenvolvimento"}, 201



def get_unfinshed_order_from_db_by_vehicle_id(vehicle_id):
#    TODO adicionar um campo que indica se a order esta aberta ou não

    last_unfinshed_order = Order.query.filter(
        Order.fk_vehicle == vehicle_id).filter(
            Order.total_value==0).first()


    return last_unfinshed_order


def update_order(unfinshed_order):

    final_hour = get_actual_hour()
    
    hour_quantity = get_hour_quantity(unfinshed_order.initial_hour)

    temp ={
        "final_hour":final_hour,
        "hour_quantity":hour_quantity,
        "total_value": hour_quantity * 1,
    }

    order_schema = OrderSchema()    
    order = order_schema.load(temp)
    current_app.db.session.add(order)
    current_app.db.session.commit()
    return False

#TODO mover para a biblioteca utils

def get_hour_quantity(initial_hour):    
    return get_actual_hour() - initial_hour 


def get_actual_hour():   
    return datetime.now().hour * 100 + datetime.now().minute


def get_actual_weekday():
    return datetime.now().weekday()
    

def get_actual_date():
    return datetime.now().date()