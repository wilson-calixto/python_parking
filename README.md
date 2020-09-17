# python_parking

An API using Python and Flask.

## To run this app you must to do the instructions above:

choose a folder to create and activate a virtual environment 

```bash
~$ python3 -m venv python_parking_venv
~$ source python_parking_venv/bin/activate
```

Access the project folder and install the necessary dependencies

```bash
~$ pip install --upgrade pip
~$ pip install -r requirements.txt
```



## How to Execute the Project

```bash
~$ export FLASK_APP=app
~$ export FLASK_ENV=Development
~$ export FLASK_DEBUG=True
~$ flask db migrate
~$ flask db upgrade
~$ flask run	
```


## How do Migrations

```bash
~$ flask db init
~$ flask db migrate
~$ flask db upgrade

```

## To run unit tests you must to do the commands above:

```bash
~$ cd tests/unit_tests 
~$ ./test_coverage.sh 
        or
~$ py.test --cov-report html *.py --cov=../../ 
        or
~$ python tests_order.py

```

after run unit test open the folder htmlcov and open the file index.html

## For use this api.

Access the url : http://127.0.0.1:5000/  using Insomnia or Postman


For add new order:
    url:
        http://127.0.0.1:5000/init_order

    payload:
        {
            "vehicle_license_plate": "ttt0000"
        }


For finish a order:
    url:
        http://127.0.0.1:5000/finish_order

    payload:
        {
            "vehicle_license_plate": "ttt0000"
        }


For get a report:
    url:
        http://127.0.0.1:5000/finish_order

    payload:
        {
            "initial_date":"2020-09-15",
            "final_date":"2020-09-17"
        }




