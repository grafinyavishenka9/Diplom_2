import pytest
from generators import *
from data import *
from methods.user_methods import UserMethods


@pytest.fixture(scope = "function")
def user_creation():
    credentials = generate_user_credentials()
    yield credentials
    
@pytest.fixture(scope = "function")
def user_login():
    credentials = generate_user_credentials()
    UserMethods.user_creation(credentials)
    credentials.pop("name")
    yield credentials
    
@pytest.fixture(scope = "function")
def order_creation():
    credentials = DataForOrderCreation.CREATE_ORDER_DATA
    yield credentials
