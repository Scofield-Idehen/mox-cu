# @pragma version 0.4.0
# @license MIT 

from interfaces import i_fav

list_of_deployed_fav_contract: public(DynArray[address, 100])
original_version: address 




@deploy

def __init__(original_version: address):
    self.original_version = original_version


@external
def create_fev():
    new_contract_Update: address = create_copy_of(self.original_version)
    self.list_of_deployed_fav_contract.append(new_contract_Update)

@external 
def store_from_contract(fav_index: uint256, new_number: uint256):
    fav_address: address = self.list_of_deployed_fav_contract[fav_index]
    fav_contract: i_fav= i_fav(fav_address)
    extcall fav_contract.store(new_number)
    
