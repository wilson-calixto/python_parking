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
    try:
        period_schema = PeriodSchema(many=True)
        period = Period.query.all()
        return period_schema.jsonify(period), 200

    except Exception as e:
        return {"error":str(e)}, 500


@bp_period.route('/period', methods=['POST'])
def add_period():
    """
    Add period in database.
    """
    try:
        #TODO tranformar cada chamada em um método de uma biblioteca
        period_schema = PeriodSchema()
        
        converted_period = conver_to_period_db(request.json)
        
        period = period_schema.load(converted_period)
        current_app.db.session.add(period)
        current_app.db.session.commit()
        return period_schema.jsonify(period), 201
    except Exception as e:
        return {"error":str(e)}, 500

def conver_to_period_db(period):
    #TODO REMOVER ESSA CONVERSAO NO FUTURO

    # print("conver_to_period_db",type(period['value_per_hour']))
    # print("dir ",dir(period))
    # print("type ",type(period))
    return period



def get_period_from_db(hour,day):
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
                Period.initial_day >= day).first()

    if (period is None):
        raise Exception("The current time does not correspond to any registered period, please enter a valid period")
    return period



def get_period_from_db_by_id(period_id):
    
    period = Period.query.filter(
        Period.period_id == period_id).first()


    return period