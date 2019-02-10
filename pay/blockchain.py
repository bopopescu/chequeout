from block import Block

class Blockchain:

    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        self.chain.append(Block({}, 0))

    def print_chain(self):
        for item in self.chain:
            print(item)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.generate_hash():
                print("The current hash of the block does not equal the generated hash of the block")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("The previous hash value of the current block is not equal to the hash of the previous block")
                return False

            return True

    def add_block(self, transactions):
        previous_hash_new_block = self.chain[-1].hash;
        new_block = Block(transactions, previous_hash_new_block)
        # you also need to get a proof of work before adding the block to the chain
        proof = self.proof_of_work(new_block, 2)
        self.chain.append(new_block)

        print(proof, new_block)
        print("PROOF OF WORK PROVIDED>>>")
        print("BLOCK HAS BEEN ADDED")

        return (proof, new_block)

    def proof_of_work(self, block, difficulty):
        proof = block.generate_hash()
        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()

        block.nonce = 0
        return proof
