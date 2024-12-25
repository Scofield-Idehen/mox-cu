from src import fav
#type list not really necessary
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network



def deploy_fav():
    fav_contract = fav.deploy() #deploy from the src directory
    start_number = fav_contract.retrieve() #function from the fav file
    print(f"Start number: {start_number}")
    
    fav_contract.store(75)
    new_number = fav_contract.retrieve()
    print(f"New number: {new_number}")
    

    active_network = get_active_network()
    if active_network.has_explorer():
        result = active_network.moccasin_verify(fav_contract)
        result.wait_for_verification()
    return fav_contract


def moccasin_main():
    deploy_fav() 