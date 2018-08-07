from json import JSONEncoder

from blockchain.block import Block
from blockchain.transaction import Transaction


class BlockChainEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Block):
            return {
                'index': o.index,
                'timestamp': o.timestamp,
                'transactions': o.transactions,
                'proof': o.proof,
                'previous_hash': o.previous_hash,
            }
        if isinstance(o, Transaction):
            return {
                'sender': o.sender,
                'recipient': o.recipient,
                'amount': o.amount,
            }
