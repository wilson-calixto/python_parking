from datetime import datetime
from .serializer import OrderSchema, Order,PeriodSchema
from sqlalchemy import func
from sqlalchemy.orm import aliased
from flask import Blueprint, jsonify, request, current_app
from .vehicles import *
from .period import *


# Blueprint init
bp_order_report = Blueprint('order_report', __name__)

@bp_order_report.route('/report', methods=['GET'])
def get_order():
    """
    Get all order in the database.
    """
    initial_date = request.json.get('initial_date')
    final_date = request.json.get('final_date')

    order_schema = OrderSchema(many=True)

    all_orders = Order.query.filter(
        Order.order_date >= initial_date).filter(
            Order.order_date <= final_date)#.group_by(
            # Order.order_date)

    print("\n",all_orders)
    #TODO otimizar esse somatorio
    my_sum = 0
    for order in all_orders:     
        print("\n",order)
   
        my_sum+=order.total_value
    
    #TODO adicionar a query abaixo;
    # SELECT order_date, SUM(total_value) As Total
    # FROM order
    # WHERE order_date between(initial_date,final_date)
    # GROUP BY order_date; 
    
    # session.query(Table.column, func.count(Table.column)).group_by(Table.column).all()
    bb = current_app.db.session.query(
         func.sum(Order.total_value).label('price')).group_by(
            Order.order_date)#.subquery()

    # print('bb',bb)

    bb = aliased(Order,alias=bb, adapt_on_names=True)

    # print('bb',dir(bb))
    # return order_schema.jsonify(bb), 201


    return {"revenues":my_sum}, 200
