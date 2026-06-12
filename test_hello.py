# test_hello.py
from hello import greet


def test_greet_world():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Jing") == "Hello, Jing!"
