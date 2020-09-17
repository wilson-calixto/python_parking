from flask import Blueprint, jsonify, request, current_app
from ..models.serializer import OrderSchema, Order

from .period import *
from .vehicles import *
from ..libs.utils import *







# Blueprint init
bp_order = Blueprint('order', __name__)

@bp_order.route('/order', methods=['GET'])
def get_order():
    try:    

        """
        Get all order in the database.
        """

        order_schema = OrderSchema(many=True)
        order = Order.query.all()
        return order_schema.jsonify(order), 200
        # TODO melhorar essa resposta
        # response = format_standard_response(success=True)
        # return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500

    

@bp_order.route('/init_order', methods=['POST'])
def add_order():
    try:    

        """
        Add order in database.
        """
        
        vehicle_license_plate = request.json.get('vehicle_license_plate')  
        checks_the_work_order_is_open(vehicle_license_plate)
        new_order_register = generate_new_order_register(vehicle_license_plate)        
        order = insert_new_order(new_order_register)
        response = format_standard_response(success=True)
        return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500

def checks_the_work_order_is_open(vehicle_license_plate):
    vehicle = get_vehicle_by_license_plate_from_db(vehicle_license_plate)

    if(vehicle is not None):
        last_order = get_opening_order_from_db_by_vehicle_id(vehicle.vehicle_id)
        if(last_order is not None):
            raise Exception("A service order is already open for this vehicle")



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

        opening_order = get_opening_order_from_db_by_vehicle_id(vehicle.vehicle_id)

        if(opening_order is None):
            raise Exception("service order not found, please check if the vehicle has already entered the system")



        last_period = get_period_from_db_by_id(opening_order.fk_period)

        
        order_update_data = generate_order_update_data(\
            opening_order.initial_hour,\
            last_period,\
            actual_hour)

        total_value = update_order(opening_order,order_update_data)

        if(requires_a_new_order(actual_hour, last_period.final_hour)):
            total_value += insert_a_complemetary_order(last_period.final_hour + 1, actual_hour, vehicle)


        current_app.db.session.commit()
        
        data={"total_value":total_value}
        response = format_custom_data_response(data=data)
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
        "order_date":actual_date,
        "status":"close"
    }

    order_schema = OrderSchema()    
    order = order_schema.load(temp)
    current_app.db.session.add(order)
    return total_value




def get_opening_order_from_db_by_vehicle_id(vehicle_id):
#    TODO adicionar um campo que indica se a order esta aberta ou não

    last_opening_order = Order.query.filter(
        Order.fk_vehicle == vehicle_id).filter(
            Order.status=='open').first()

    return last_opening_order


def update_order(opening_order,args):
    temp ={
        "final_hour": args['final_hour'],
        "hour_quantity": args['hour_quantity'],
        "total_value": args['parcial_value'],
        "status":"close"
    }

    q_result = Order.query.filter(
        Order.order_id == opening_order.order_id).update(
            temp)

    return args['parcial_value']




