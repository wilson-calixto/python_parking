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
    actual_hour = get_actual_hour()

    vehicle = get_vehicle_by_license_plate_from_db(request.json.get('vehicle_license_plate'))

    unfinshed_order = get_unfinshed_order_from_db_by_vehicle_id(vehicle.vehicle_id)

    last_period = get_period_from_db_by_id(unfinshed_order.fk_period)

    args={}
    
    args['final_hour'] = get_final_hour(last_period.final_hour, actual_hour)

    args['hour_quantity'] = get_hour_quantity(unfinshed_order.initial_hour,args['final_hour'])
    
    args['parcial_value'] = args['hour_quantity'] * last_period.value_per_hour


    total_value = update_order(unfinshed_order,args)

    if(requires_a_new_order(actual_hour, last_period.final_hour)):
        total_value += insert_a_complemetary_order(last_period.final_hour + 1, actual_hour, vehicle)


    current_app.db.session.commit()
    
    return {"total_value":total_value}, 201


def insert_a_complemetary_order(initial_hour, actual_hour,vehicle):


    # TODO melhorar isso


    actual_day = get_actual_weekday()
    
    actual_date = get_actual_date()

    complementary_period = get_period_from_db(initial_hour,actual_day)

    final_hour = get_final_hour(actual_hour,complementary_period.final_hour)

    hour_quantity = get_hour_quantity(initial_hour,final_hour)


    total_value = hour_quantity * complementary_period.value_per_hour


    temp ={
        "fk_vehicle":vehicle.vehicle_id,
        "fk_period":complementary_period.period_id,
        "initial_hour":initial_hour,
        "final_hour":final_hour,
        "hour_quantity":hour_quantity,
        "total_value": total_value,
        "order_date":actual_date
    }

    order_schema = OrderSchema()    
    order = order_schema.load(temp)
    current_app.db.session.add(order)
    return total_value




def get_unfinshed_order_from_db_by_vehicle_id(vehicle_id):
#    TODO adicionar um campo que indica se a order esta aberta ou não

    last_unfinshed_order = Order.query.filter(
        Order.fk_vehicle == vehicle_id).filter(
            Order.total_value==0).first()


    return last_unfinshed_order


def update_order(unfinshed_order,args):


    temp ={
        "final_hour": args['final_hour'],
        "hour_quantity": args['hour_quantity'],
        "total_value": args['parcial_value'],
    }



    q_result = Order.query.filter(
        Order.order_id == unfinshed_order.order_id).update(
            temp)

    return args['parcial_value']



#TODO mover para a biblioteca utils

def get_final_hour(actual_hour,last_period_hour):  
    if(requires_a_new_order(actual_hour, last_period_hour)):
        return last_period_hour

    return actual_hour

def requires_a_new_order(actual_hour, last_period_hour):
    # TODO tratar esse erro
    if(actual_hour>1800):
        return False
    
    return actual_hour > last_period_hour



def get_hour_quantity(initial_hour,final_hour):    
    diference = final_hour - initial_hour
    if(diference < 100):
        return 1
    else:
        return  round(diference/100)


def get_actual_hour():   
    return 8 * 100
    # return 18 * 100
    # return datetime.now().hour * 100 + datetime.now().minute


def get_actual_weekday():
    return datetime.now().weekday()
    

def get_actual_date():
    return datetime.now().date()