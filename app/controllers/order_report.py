from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import aliased
from flask import Blueprint, jsonify, request, current_app
from sqlalchemy import DDL


from .period import *
from ..libs.utils import *
from ..models.serializer import OrderSchema, Order,PeriodSchema

# Blueprint init
bp_order_report = Blueprint('order_report', __name__)

@bp_order_report.route('/report', methods=['GET'])
def get_orders_group_by_day():
    """
    Get all order in the database group by day.
    """

    try:
        initial_date = request.json.get('initial_date')
        final_date = request.json.get('final_date')

        order_schema = OrderSchema(many=True)

        all_orders = current_app.db.session.query(\
            Order.order_date.label('date'), \
                func.sum(Order.total_value).label('revenues'))\
                    .group_by(Order.order_date).all()

                
        print("all_orders\n",type(all_orders))

        data_result = mount_order_data_result(all_orders)

        response = format_custom_data_response(data=data_result)
        return response, 201

    except Exception as e:
        response = format_standard_response(success=False,error=str(e))
        return response, 500

def mount_order_data_result(all_orders):
    my_sum = 0
    message={}

    order_schema = OrderSchema(many=True)


    converted_order=[]
    #TODO melhorar esse metodo de conversao adicionando jsonify

    
    for order in all_orders:
        temp_message={}
        temp_message["date"] = order[0] 
        temp_message["revenues"] = order[1]         
        converted_order.append(temp_message)


    return converted_order