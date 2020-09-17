from os.path import dirname, abspath, join

basedir = abspath(dirname(__file__))
#TODO resolver erro na migration do banco
# TEST_DB='database_test.db'
TEST_DB='database.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir, TEST_DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'secretkey'


# TESTING = True
# WTF_CSRF_ENABLED = False
# DEBUG = False

