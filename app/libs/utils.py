from datetime import datetime


def get_final_hour(actual_hour,last_period_hour):  
    if(requires_a_new_order(actual_hour, last_period_hour)):
        return last_period_hour

    return actual_hour

def requires_a_new_order(actual_hour, last_period_hour):
    # TODO tratar esse erro
    if(actual_hour>1800):
        return False
    
    return actual_hour > last_period_hour



def get_hour_quantity(initial_hour,final_hour):    
    diference = final_hour - initial_hour
    if(diference < 100):
        return 1
    else:
        return  round(diference/100)


def get_actual_hour():   
    # return 8 * 100
    # return 18 * 100
    return datetime.now().hour * 100 + datetime.now().minute


def get_actual_weekday():
    return datetime.now().weekday()
    

def get_actual_date():
    return datetime.now().date()


def format_standard_response(success,error=None):
    if(success):
        return {"message":"Operation performed successfully",\
                    "error":error
            }

    return {"message":"Error when performing operation",\
            "error":error
            }

def format_custom_response(message,error=None):
    return {"message":message,\
                "error":error
        }
      