from vyper import compile_code
from web3 import Web3

MY_ADDRESS = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
PRICE_FEED_ADDRESS = "0x694AA1769357215DE4FAC081bf1f309aDC325306"

def main():
    print("hello world!")
    with open("fav.vy", "r") as f:
        fav_code = f.read() 
        com_details = compile_code(fav_code, output_formats=["bytecode", "abi"])
        print(com_details)

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    fv_contract= w3.eth.contract(bytecode=com_details["bytecode"], abi=com_details["abi"])
    print(fv_contract)

    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = fv_contract.constructor(PRICE_FEED_ADDRESS).build_transaction(
       { 
           "nonce": nonce,
           "from": MY_ADDRESS,
           "getPrice": w3.eth.gas_price
       }
    )
    print(transaction)


if __name__ == "__main__":
    main()