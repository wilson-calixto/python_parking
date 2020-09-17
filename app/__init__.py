from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import event
from .model import configure_database
from .serializer import configure_marshmallow
from .products import bp_products
from .vehicles import bp_vehicles
from .period import bp_period
from .order import bp_order
from .order_report import bp_order_report

from .model import Period


def create_app():
    """
    app factory function.
    """

    app = Flask(__name__)
    app.config.from_object('config')

    configure_database(app)
    configure_marshmallow(app)

    Migrate(app, app.db)


    app.register_blueprint(bp_products)


    app.register_blueprint(bp_vehicles)
    app.register_blueprint(bp_period)
    app.register_blueprint(bp_order)
    app.register_blueprint(bp_order_report)
    # insert_initial_values(app.db)
    
    
    return app



def insert_initial_values(*args, **kwargs):
    print('\n\n\insert_initial_values\n\n\n')
    app.db.session.add(Period(generate_first_period_data()))
    app.db.session.add(Period(generate_second_period_data()))
    app.db.session.add(Period(generate_third_period_data()))
    app.db.session.commit()
    print('\n\n\insert_initial_values\n\n\n')

event.listen(Period.__table__, 'after_create', insert_initial_values)

def generate_first_period_data():

    period = {
        "initial_day": 0,
        "final_day": 4,
        "initial_hour": 800,
        "final_hour": 1200,
        "value_per_hour": 2.00
    }
    return period

def generate_second_period_data():

    period = {
        "initial_day": 0,
        "final_day": 4,
        "initial_hour": 1201,
        "final_hour": 1800,
        "value_per_hour": 4.00
    }
    return period

def generate_third_period_data():

    period = {
        "initial_day": 5,
        "final_day": 6,
        "initial_hour": 800,
        "final_hour": 1800,
        "value_per_hour": 2.50
    }
    return period