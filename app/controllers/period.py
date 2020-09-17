from ..models.model import Period

from ..models.serializer import PeriodSchema

from flask import Blueprint, jsonify, request, current_app
from ..libs.utils import *

# Blueprint init
bp_period = Blueprint('period', __name__)

@bp_period.route('/period', methods=['GET'])
def get_period():
    """
    Get all period in the database.
    """
    try:
        period_schema = PeriodSchema(many=True)
        period = Period.query.all()
        
        # TODO melhorar essa resposta
        # response = format_custom_data_response(data=period_schema.jsonify(period))
        response = period_schema.jsonify(period)
        return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500


@bp_period.route('/period', methods=['POST'])
def add_period():
    """
    Add period in database.
    """
    try:
        #TODO tranformar cada chamada em um método de uma biblioteca
        new_period = add_new_period(request.json)
        
        response = format_standard_response(success=True)
        return response, 201
    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500

def add_new_period(new_period):
    period_schema = PeriodSchema()
    period = period_schema.load(new_period)
    current_app.db.session.add(period)
    current_app.db.session.commit()
    return period_schema.jsonify(period)


def get_period_from_db(hour,day):
    print('hour,day',hour,day)
    # days seg == 0 ... dom == 6
    # hous 800 == 8:00 .... 1800 == 18:00 

    # from datetime import datetime, timedelta

    # TODO trocar as horas de interger por  datetime
    # now = datetime.now()
    # eight_hours_ago = now - timedelta(hours=8)

    # period = Period.query.filter(Period.initial_hour >= hour).filter(Period.initial_day >= day).first()

    period = Period.query.filter(
        Period.initial_hour <= hour).filter(
            Period.final_hour >= hour).filter(
                Period.initial_day <= day).filter(
                    Period.final_day >= day).first()

    if (period is None):
        raise Exception("The current time does not correspond to any registered period, please enter a valid period")
    return period



def get_period_from_db_by_id(period_id):
    
    period = Period.query.filter(
        Period.period_id == period_id).first()


    return period