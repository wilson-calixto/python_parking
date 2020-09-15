from .model import Product
from .model import Vehicle
from .model import Period,Teste_order
from .model import Order


from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

marshmallow = Marshmallow()

def configure_marshmallow(app):
    marshmallow.init_app(app)


class ProductSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True  # Optional: deserialize to model instances

        fields = ('product_id','name', 'description', 'price', 'quantity')
    product_id = auto_field()

class VehicleSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Vehicle
        load_instance = True  # Optional: deserialize to model instances

    vehicle_id = auto_field()
    vehicle_license_plate = auto_field()

class PeriodSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Period
        load_instance = True  # Optional: deserialize to model instances
        fields = ('period_id','initial_day','final_day','initial_hour','final_hour','value_per_hour')
    period_id = auto_field()



class Teste_orderSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Teste_order
        load_instance = True  # Optional: deserialize to model instances
        fields = ('teste_order_id','initial_day','final_day','initial_hour','final_hour','value_per_hour')
    teste_order_id = auto_field()
# fields = ('order_id','fk_vehicle','fk_period','initial_hour','final_hour','hour_quantity','total_value','order_date')






class OrderSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Order
        load_instance = True  # Optional: deserialize to model instances
        fields = ('order_id','fk_vehicle','fk_period','initial_hour','final_hour','hour_quantity','total_value','order_date')
    order_id = auto_field()

