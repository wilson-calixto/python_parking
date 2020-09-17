import sys
sys.path.append('../..')
import os
import unittest
import json 

from app import *

class BasicTests(unittest.TestCase):
 

    def setUp(self):
        app = create_app(custom_config='config_for_tests')
        self.app = app.test_client()


    def test_finish_a_order(self,vehicle_license_plate="ttt0000"):
        
        payload = '{"vehicle_license_plate":'+vehicle_license_plate+'}'

            # insert a order
        response_temp = self.app.post('/init_order',json=json.loads(payload))

            # finish a order
        response = self.app.post('/finish_order',json=json.loads(payload))
        response_json = json.loads(response.data)
        
        self.assertEqual(response.status_code, 201)
        self.assertIs(response_json['data']['total_value'], float)



    def test_get_order_report_with_records(self):
        self.test_finish_a_order(vehicle_license_plate="nnn1111")
        
        date = get_actual_date()        
        payload = '{"initial_date":'+date+',"final_date":'+date+'}'
        
        response = self.app.get('/report',json=json.loads(payload))        
        response_json = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertIs(response_json['data']['revenues'], float)

        
 
 

    def test_get_order_report_without_records(self):
        payload = '{"initial_date":"2001-09-15","final_date":"2001-09-17"}'
        response = self.app.get('/report',json=json.loads(payload))        
        response_json = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['message'], "No records found, please check the selected dates.")

    def test_get_order_report_with_invalid_data_interval(self):
        payload = '{"initial_date":"2020-09-30","final_date":"2020-09-01"}'
        response = self.app.get('/report',json=json.loads(payload))
        response_json = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['message'], "No records found, please check the selected dates.")

    def test_get_order_report_with_invalid_data_format(self):
        payload = '{"initial_date":"2020-094646-15","final_date":"2020-094646-15"}'
        response = self.app.get('/report',json=json.loads(payload))
        response_json = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['message'], "No records found, please check the selected dates.")

    def test_finish_a_order2(self,vehicle_license_plate="ttt0000"):
        
        payload = '{"vehicle_license_plate":"ttt0000"}'

            # insert a order
        response_temp = self.app.post('/init_order',json=json.loads(payload))

            # finish a order
        response = self.app.post('/finish_order',json=json.loads(payload))
        response_json = json.loads(response.data)
        
        self.assertEqual(response.status_code, 201)
        
def get_actual_date():
    return datetime.now().date()


if __name__ == "__main__":
    unittest.main()