from script.deploy import deploy_fav
import pytest

@pytest.fixture(scope="session") #scope = "function"
def fev_contract():
    return deploy_fav()