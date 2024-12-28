from script.deploy import deploy_coffee
import pytest
from script.deploy_mocks import deploy_feed
from moccasin.config import get_active_network


@pytest.fixture(scope="session") #scope = "function"
def eth_coffee():     #remember to change this
    return deploy_feed()

@pytest.fixture(scope="function") #scope = "function"
def deployer():
    return get_active_network().get_default_account()



@pytest.fixture(scope="function") #scope = "function"
def coffee(eth_coffee):
    return deploy_coffee(eth_coffee)