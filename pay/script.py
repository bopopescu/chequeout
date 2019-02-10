import block
import blockchain
from hashlib import sha256

def process_request():
    with open("transaction.csv", "r") as f:
        data = f.read()
        items = data.split(',')
        transaction = {}
        print(items)
        transaction['name'] = items[0]
        transaction['recipient'] = items[1]
        transaction['amount'] = items[2]
        transaction['username'] = items[3]
        transaction['account_number'] = items[4]
        transaction['card_number'] = items[5]
        transaction['cvv'] = items[6]
        return transaction
    return

def work_flow():
    chain = blockchain.Blockchain()
    while(True):
        print("Menu")
        print("---> process new transaction")
        print("---> view blockchain")

        choice = int(input())

        if(choice == 1):
            chain.add_block(process_request())
        else:
            chain.print_chain()
