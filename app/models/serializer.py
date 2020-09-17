from .model import Vehicle
from .model import Period
from .model import Order


from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

marshmallow = Marshmallow()

def configure_marshmallow(app):
    marshmallow.init_app(app)



class VehicleSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Vehicle
        load_instance = True 

    vehicle_id = auto_field()
    vehicle_license_plate = auto_field()


class PeriodSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Period
        load_instance = True 
        fields = ('period_id','initial_day','final_day','initial_hour','final_hour','value_per_hour')
    period_id = auto_field()



class OrderSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Order
        load_instance = True 
        fields = ('order_id','fk_vehicle','fk_period','initial_hour','final_hour','hour_quantity','total_value','order_date','status')
    order_id = auto_field()
    status = auto_field()

