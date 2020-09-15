from .model import Vehicle

from .serializer import VehicleSchema

from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_vehicles = Blueprint('vehicles', __name__)

@bp_vehicles.route('/vehicle', methods=['GET'])
def get_vehicles():
    """
    Get all vehicles in the database.
    """

    vehicle_schema = VehicleSchema(many=True)
    vehicle = Vehicle.query.all()
    return vehicle_schema.jsonify(vehicle), 200



@bp_vehicles.route('/vehicle', methods=['POST'])
def add_vehicle():
    """
    Add vehicle in database.
    """

    vehicle_schema = VehicleSchema()
    vehicle = vehicle_schema.load(request.json)
    current_app.db.session.add(vehicle)
    current_app.db.session.commit()
    return vehicle_schema.jsonify(vehicle), 201








    
    # else:
    #     return jsonify(error), 401
