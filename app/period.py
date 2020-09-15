from .model import Period

from .serializer import PeriodSchema

from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_period = Blueprint('period', __name__)

@bp_period.route('/period', methods=['GET'])
def get_period():
    """
    Get all period in the database.
    """

    period_schema = PeriodSchema(many=True)
    period = Period.query.all()
    return period_schema.jsonify(period), 200
