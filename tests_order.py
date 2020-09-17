import os
import unittest
from app import * 
import json 
 
class BasicTests(unittest.TestCase):
 

    def setUp(self):
        app = create_app(custom_config='config_for_tests')
        self.app = app.test_client()

 
    # def test_insert_a_order(self):

    #     response = self.app.post('/init_order',data=dict(vehicle_license_plate='awwz7825'))
    #     print("response",dir(response))
    #     self.assertEqual(response.status_code, 201)
 

    # def test_finish_a_order(self):
    #     response = self.app.post('/finish_order',data=dict(vehicle_license_plate='awwz7825'))
    #     print("response",dir(response))
    #     self.assertEqual(response.status_code, 201)



    # def test_get_order_report(self):
        # json_send_data = dict(initial_date="2020-09-15",final_date="2020-09-17")
    #     response = self.app.get('/report',data=json_send_data, follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)
        
 
 

    def test_get_order_report(self):
        payload = '{"initial_date":"2020-09-15","final_date":"2020-09-17"}'
        response = self.app.get('/report',json=json.loads(payload))
        self.assertEqual(response.status_code, 201)
 
 
if __name__ == "__main__":
    unittest.main()