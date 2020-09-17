from .model import Vehicle

from .serializer import VehicleSchema

from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_vehicles = Blueprint('vehicles', __name__)

@bp_vehicles.route('/vehicle', methods=['GET'])
def get_vehicles():
    # return get_all_vehicles_from_db(), 200

    try:
        return get_all_vehicles_from_db(), 200
    except Exception as e:
        return {"error":str(e)}, 500
        
@bp_vehicles.route('/vehicle', methods=['POST'])
def add_vehicle():
    try:
        added_vehicle = add_vehicle_in_bd(request.json)
        
        return vehicle_schema.jsonify(added_vehicle) , 201
    except Exception as e:
        return {"error":str(e)}, 500
    

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
