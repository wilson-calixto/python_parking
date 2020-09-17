from .serializer import OrderSchema, Order
from flask import Blueprint, jsonify, request, current_app

from .period import *
from .libs.utils import *


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
    try:    

        """
        Add order in database.
        """
        
        vehicle_license_plate = request.json.get('vehicle_license_plate')                
        new_order_register = generate_new_order_register(vehicle_license_plate)        
        order = insert_new_order(new_order_register)
        response = format_standard_response(success=True)
        return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500



def generate_new_order_register(vehicle_license_plate):
     
    
    vehicle = get_vehicle_by_license_plate_from_db(vehicle_license_plate)
    if(vehicle is None):            
        vehicle = add_vehicle_in_bd({"vehicle_license_plate": vehicle_license_plate})        

    actual_hour = get_actual_hour()
    actual_day = get_actual_weekday()
    actual_date = get_actual_date()


    first_period = get_period_from_db(hour=actual_hour,day=actual_day)


    new_order ={
        "fk_vehicle":vehicle.vehicle_id,
        "fk_period":first_period.period_id,
        "initial_hour":actual_hour,
        "final_hour":0,
        "hour_quantity":0,
        "total_value":0,
        "order_date":actual_date
    }

    return new_order

def insert_new_order(new_order_register):

    order_schema = OrderSchema()    
    order_result = order_schema.load(new_order_register)
    current_app.db.session.add(order_result)
    current_app.db.session.commit()
    
    return order_schema.jsonify(order_result)

    
@bp_order.route('/finish_order', methods=['POST'])
def finish_order():
    try:    

        """
        Add order in database.
        """
        # TODO adicionar tratamento de erro
        # TODO refatorar e adicionar funções pequenas
        actual_hour = get_actual_hour()

        vehicle = get_vehicle_by_license_plate_from_db(request.json.get('vehicle_license_plate'))

        unfinshed_order = get_unfinshed_order_from_db_by_vehicle_id(vehicle.vehicle_id)

        last_period = get_period_from_db_by_id(unfinshed_order.fk_period)

        
        order_update_data = generate_order_update_data(\
            unfinshed_order.initial_hour,\
            last_period,\
            actual_hour)

        total_value = update_order(unfinshed_order,order_update_data)

        if(requires_a_new_order(actual_hour, last_period.final_hour)):
            total_value += insert_a_complemetary_order(last_period.final_hour + 1, actual_hour, vehicle)


        current_app.db.session.commit()
        
        message={"total_value":total_value}
        response = format_custom_response(message=message)
        return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500


def generate_order_update_data(initial_hour,last_period,actual_hour):         
    args={}
    args['final_hour'] = get_final_hour(last_period.final_hour, actual_hour)

    args['hour_quantity'] = get_hour_quantity(initial_hour,args['final_hour'])
    
    args['parcial_value'] = args['hour_quantity'] * last_period.value_per_hour

    return args


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




