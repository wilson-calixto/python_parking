from .model import Vehicle

from .serializer import VehicleSchema

from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_vehicles = Blueprint('vehicles', __name__)

@bp_vehicles.route('/vehicle', methods=['GET'])
def get_vehicles():
    return get_all_vehicles_from_db(), 200

@bp_vehicles.route('/vehicle', methods=['POST'])
def add_vehicle():
    return add_vehicle_in_bd()

def get_all_vehicles_from_db():

    """
    Get all vehicles in the database.
    """

    vehicle_schema = VehicleSchema(many=True)
    vehicle = Vehicle.query.all()
    return vehicle_schema.jsonify(vehicle), 200




def add_vehicle_in_bd():
    """
    Add vehicle in database.
    """

    vehicle_schema = VehicleSchema()
    vehicle = vehicle_schema.load(request.json)
    current_app.db.session.add(vehicle)
    current_app.db.session.commit()
    return vehicle_schema.jsonify(vehicle), 201








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
