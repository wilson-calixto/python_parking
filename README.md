# python_parking

to run this app you must to do the commands above :

python3 -m venv python_parking_venv
source python_parking_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=crudapp.py
flask db init
flask db migrate -m "entries table"






OLD:
mysql -u root
CREATE USER 'dt_admin'@'local_host' IDENTIFIED BY 'dt_746_@_#_Python_Parking';
CREATE DATABASE python_parking_db;

GRANT ALL PRIVILEGES ON python_parking_db.* TO 'dt_admin'@'localhost' IDENTIFIED BY 'dt_746_@_#_Python_Parking';
