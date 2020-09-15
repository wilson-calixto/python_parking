# python_parking

to run this app you must to do the commands above :

python3 -m venv python_parking_venv

source python_parking_venv/bin/activate
pip install --upgrade pip
pip install -r Requirements.txt
export FLASK_APP=app

flask db init


flask db migrate -m "entries table"

flask db upgrade

flask run



OLD:
mysql -u root
CREATE USER 'dt_admin'@'local_host' IDENTIFIED BY 'dt_746_@_#_Python_Parking';
CREATE DATABASE python_parking_db;

GRANT ALL PRIVILEGES ON python_parking_db.* TO 'dt_admin'@'localhost' IDENTIFIED BY 'dt_746_@_#_Python_Parking';
