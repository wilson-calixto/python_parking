from .model import Product
from .model import Car
from .model import Period
from .model import Order


from flask_marshmallow import Marshmallow


marshmallow = Marshmallow()

def configure_marshmallow(app):
    marshmallow.init_app(app)


class ProductSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Product
        fields = ('product_id','name', 'description', 'price', 'quantity')

class CarSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Car
        fields = ('car_id', 'vehicle_license_plate')


class PeriodSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Period
        fields = ('period_id','initial_day','final_day','initial_hour','final_hour','value_per_hour')


class OrderSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Order
        fields = (
        'order_id',
        'fk_vehicle',
        'fk_period',
        'initial_hour',
        'final_hour',
        'hour_quantity',
        'total_value',
        'order_date')
