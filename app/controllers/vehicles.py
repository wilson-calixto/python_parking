from ..models.model import Vehicle

from ..models.serializer import VehicleSchema

from ..libs.utils import *

from flask import Blueprint, jsonify, request, current_app


def get_vehicles():
    try:       
        all_vehicles = get_all_vehicles_from_db()
        #TODO melhorar esse get
        message = {'vehicles':all_vehicles}
        response = format_custom_message_response(message = message)
        
        return all_vehicles, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500
        
def add_vehicle():
    try:
        added_vehicle = add_vehicle_in_bd(request.json)
        response = format_standard_response(success=True)
        return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500
    

def get_all_vehicles_from_db():

    """
    Get all vehicles in the database.
    """

    vehicle_schema = VehicleSchema(many=True)
    vehicle = Vehicle.query.all()

    return vehicle_schema.jsonify(vehicle)




def add_vehicle_in_bd(new_vehicle):
    """
    Add vehicle in database.
    """

    vehicle_schema = VehicleSchema()
    vehicle = vehicle_schema.load(new_vehicle)
    current_app.db.session.add(vehicle)
    current_app.db.session.commit()
    return vehicle








def get_vehicle_by_license_plate_from_db(vehicle_license_plate):

    """
    Get one vehicles in the database.
    """
    try:

        vehicle_schema = VehicleSchema()
        vehicle = Vehicle.query.filter_by(vehicle_license_plate=vehicle_license_plate).first()

        return vehicle
    except Exception:
        raise Exception('Could not find the vehicle_license_plate.')
