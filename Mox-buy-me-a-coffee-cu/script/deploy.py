
from moccasin.config import get_active_network
from src import buy_me_a_coffee
from script.deploy_mocks import deploy_feed
from moccasin.boa_tools import VyperContract

'''def deploy_coffee(price_feed: str):
    buy_me_a_coffee.deploy(price_feed)'''
    
    

def moccasin_main():
    activeNetwork = get_active_network()
    price_feed: VyperContract = activeNetwork.manifest_named('price_feed')
    print(f"on network: {activeNetwork.name} also the network address: {price_feed.address}")




    '''price_feed = deploy_feed() # this takes two value arguments, STARTING_DECIMAL and STARTING_PRICE
    coffee = buy_me_a_coffee.deploy(price_feed) #the value is coming from getPrice 
    print(f"Coffee contract deployed to {coffee.address}")

    print(coffee.get_eth_to_usd_rate(1000))
    print(coffee.get_price(4000))
'''