from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def configure_database(app):
    db.init_app(app)
    app.db = db


class Vehicle(db.Model):
    """
    Vehicle Model Class.
    """

    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, primary_key=True)#, autoincrement=True)
    vehicle_license_plate = db.Column(db.String)

    def __init__(self, vehicle_license_plate):
        self.vehicle_license_plate = vehicle_license_plate
        

    def __repr__(self):
        return f'<Vehicle {self.vehicle_license_plate}>'



class Period(db.Model):
    """
    Period Model Class.
    """

    __tablename__ = 'period'

    period_id = db.Column(db.Integer, primary_key=True)
    initial_day = db.Column(db.Integer)
    final_day = db.Column(db.Integer)
    
    initial_hour = db.Column(db.Integer)
    final_hour = db.Column(db.Integer)
    value_per_hour = db.Column(db.Float)

    

    def __init__(self, initial_day,final_day,initial_hour,final_hour,value_per_hour):
        self.initial_day = initial_day
        self.final_day = final_day
        self.initial_hour = initial_hour
        self.final_hour = final_hour
        self.value_per_hour = value_per_hour

    def __repr__(self):
        #TODO Melhorar esses prints
        return f'<Period {self.initial_day}>'







class Order(db.Model):
    """
    Order Model Class.
    """

    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True)#, autoincrement=True)
    #TODO adicionar chave estrangeira no banco de dados

    fk_vehicle = db.Column(db.Integer)
    fk_vehicle = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'))
    fk_period = db.Column(db.Integer, db.ForeignKey('period.period_id'))
    initial_hour = db.Column(db.Integer)
    final_hour = db.Column(db.Integer)
    hour_quantity = db.Column(db.Float)
    total_value = db.Column(db.Float)
    order_date = db.Column(db.String)

    status = db.Column(db.String, default='open')


    def __init__(self,fk_vehicle,fk_period,initial_hour,final_hour,hour_quantity,total_value,order_date):
        self.fk_vehicle = fk_vehicle
        self.fk_period = fk_period
        self.initial_hour = initial_hour
        self.final_hour = final_hour
        self.hour_quantity = hour_quantity
        self.total_value = total_value
        self.order_date = order_date


    def __repr__(self):
        return f'<Order {self.order_date}>'



