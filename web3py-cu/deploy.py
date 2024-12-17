from vyper import compile_code
from web3 import Web3

def main():
    print("hello world!")
    with open("fav.vy", "r") as f:
        fav_code = f.read() 
        com_details = compile_code(fav_code, output_formats=["bytecode", "abi"])
        print(com_details)

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    fv_contract= w3.eth.contract(bytecode=com_details["bytecode"], abi=com_details["abi"],)
    print(fv_contract)

    transaction = fv_contract.constructor().build_transaction()
    print(transaction)


if __name__ == "__main__":
    main()