import pytest

@pytest.fixture()

def setup():
    print("please open the application")
    yield
    print("after your work close the browser")



