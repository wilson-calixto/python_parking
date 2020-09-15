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



@bp_period.route('/period', methods=['POST'])
def add_period():
    """
    Add period in database.
    """
    #TODO tranformar cada chamada em um método de uma biblioteca
    period_schema = PeriodSchema()
    period = period_schema.load(request.json)
    current_app.db.session.add(period)
    current_app.db.session.commit()
    return period_schema.jsonify(period), 201





def get_period_from_db(hour,day):
    # days dom == 1 ... sab == 7
    # hous 8 == 8:00 .... 18 == 18:00 

    period_schema = PeriodSchema(many=True)
    period = Period.query.filter_by(
        final_hour = hour ,
        
        initial_day  = day 

        ).first()


        # final_hour <= hour ,
        # initial_hour >= hour ,
        # initial_day  <= day ,
        # final_day >= day  
    return period