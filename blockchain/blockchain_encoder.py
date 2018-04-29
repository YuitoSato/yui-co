from json import JSONEncoder

from blockchain.block import Block


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
