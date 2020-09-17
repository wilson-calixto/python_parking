# python_parking

An API using Python and Flask.

## To run this app you must to do the commands above:

python3 -m venv python_parking_venv

source python_parking_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


## How to Execute the Project

```bash
~$ export FLASK_APP=app
~$ export FLASK_ENV=Development
~$ export FLASK_DEBUG=True
~$ flask db init
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
~$ python tests_order.py 

```