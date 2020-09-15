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
