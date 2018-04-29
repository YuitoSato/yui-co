from time import time


class Block:
    def __init__(self, index, transactions, proof, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = time()
        self.proof = proof
        self.previous_hash = previous_hash
