from .model import Car

from .serializer import CarSchema

from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_cars = Blueprint('cars', __name__)

@bp_cars.route('/car', methods=['GET'])
def get_cars():
    """
    Get all cars in the database.
    """

    car_schema = CarSchema(many=True)
    car = Car.query.all()
    return car_schema.jsonify(car), 200
