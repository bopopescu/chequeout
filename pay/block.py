from hashlib import sha256

class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.nonce = 0
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def __repr__(self):
        text = ''
        for i in range(80):
            text += '-'
        text+='\n'
        text += "transactions:\n"
        for i in self.transactions.values():
            text += str(i)
        text+='\n'
        text +="Hash: " + str(self.hash) + '\n'
        text += "Previous Hash: " + str(self.previous_hash) + '\n'
        return text

    def generate_hash(self):
        hash_string = str(self.transactions) + str(self.nonce) + str(self.previous_hash)
        hash = sha256(hash_string.encode()).hexdigest()
        return hash
