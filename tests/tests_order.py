
from ..app import *

def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/report")
    assert response.data == b"Hello, World!"

def test_hello2(client):
    response = client.get("/order")
    assert response.data == b"Hello, World!"    