import time
from typing import TypeVar, Generic

import block

T = TypeVar('T')


class Blockchain():
    """
    simple Implementation of a blockchain
    """
    chain: [block]

    def add_data(self, data: Generic[T]):
        prev_hash = self.chain[len(self.chain) - 1].this_hash
        bl = block.Block(prev_hash, data, time.time())
        bl.mine_this_block()
        self.chain.append(bl)

    def validate_blockchain(self):
        """
        Validates the blockchain
        """
        mine_cond = self.chain[0].MINE_COND
        # Check all Blocks
        for i in range(0, len(self.chain)):
            # check if the mining condition is met
            if mine_cond not in self.chain[i].this_hash:
                return False
            # check if the hash belongs to the block
            if self.chain[i].calc_hash() != self.chain[i].this_hash:
                return False
            # for all blocks except the genesis block, check if the previous hash is correct
            if i > 0:
                if self.chain[i-1].this_hash not in self.chain[i].prev_hash:
                    print()
                    return False
        return True

    def __init__(self, data: Generic[T]):
        self.chain = []
        genesis_block = block.Block('apvs', data, time.time())
        genesis_block.mine_this_block()
        self.chain.append(genesis_block)

    def __str__(self):
        ret_string = ''
        for i in range(0, len(self.chain)):
            ret_string += '[\n'
            ret_string += str(self.chain[i])
            ret_string += '\n]\n'
        return ret_string
