from eth_utils import to_wei
import boa

SEND_VALUE = to_wei(1, "ether")
RANDOM_OWNER = boa.env.generate_address("Not_owner")

def test_price_is_correct(coffee, eth_coffee):
    assert coffee.priceFeed() == eth_coffee.address

def test_owner_is_correct(coffee, deployer):
    assert coffee.min_USD() == to_wei(5, "ether")
    assert coffee.owner() == deployer.address

def test_fund_updates_funders(coffee, deployer):
    # Arrange
    account = deployer
    # Act
    coffee.fund(sender=account.address, value=to_wei(1, "ether"))
    # Assert
    assert coffee.funders(0) == account.address

def test_default_fallback_function(coffee):
    with boa.reverts():
        coffee.fund()


def test_with_moneys(coffee, deployer):
    boa.env.set_balance(deployer.address, SEND_VALUE)
    #act
    coffee.fund(value=SEND_VALUE)
    #assert
    funder = coffee.funders(0)
    assert funder == deployer.address
    assert coffee.funder_to_funders(funder) == SEND_VALUE

def test_Onwer_cannot_withdraw(coffee, deployer):
    boa.env.set_balance(deployer.address, SEND_VALUE) #set address and give eth value 
    #act
    coffee.fund(value=SEND_VALUE)

    with boa.env.prank(RANDOM_OWNER):
        with boa.reverts():
            coffee.withdraw()

def test_owner_can_withdraw(coffee, deployer):
    boa.env.set_balance(coffee.owner(), SEND_VALUE)
    with boa.env.prank(coffee.owner()):
        coffee.fund(value= SEND_VALUE)
        coffee.withdraw()
    assert boa.env.get_balance(coffee.address) == 0