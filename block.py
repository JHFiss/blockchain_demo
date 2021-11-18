import string
import hashlib
from typing import TypeVar, Generic

T = TypeVar('T')


class Block(Generic[T]):
    """
    Implementation of a block for a blockchain that can contain arbitrary data
    """
    this_hash: string
    prev_hash: string
    data: T
    time_stamp: int
    nonce = 0

    def calc_hash(self):
        """
        Generates a hash for a block instance
        """
        hash_data = self.prev_hash + str(self.data) + str(self.time_stamp) + str(self.nonce)
        return hashlib.sha3_256(hash_data.encode('utf-8')).hexdigest()

    def mine_this_block(self):
        """
        Proof of work function for a block
        Generates new hashes and increases nonce until the created hash contains the value defined in ``mine_cond``
        """
        mine_cond: string = '300597'
        mine_hash: string = self.calc_hash()
        while mine_cond not in mine_hash:
            self.nonce += 1
            mine_hash = self.calc_hash()
            # Print the current value of nonce for debug and demonstration purposes
            print(self.nonce)
        self.this_hash = mine_hash
        return mine_hash

    def __init__(self, prev_hash: string, data: T, timestamp: int):
        self.prev_hash = prev_hash
        self.data = data
        self.time_stamp = timestamp
        self.this_hash = self.calc_hash()

        # print the values of a block after initialisation for debug and demonstration purposes
        print(self.this_hash)
        print(self.prev_hash)
        print(self.data)
        print(self.time_stamp)

    def __str__(self):
        ret = ''
        ret += '{\n'
        ret += 'previous Hash: ' + self.prev_hash + '\n'
        ret += 'Hash: ' + self.this_hash + '\n'
        ret += 'Data: ' + str(self.data) + '\n'
        ret += 'Nonce: ' + str(self.nonce) + '\n'
        ret += 'Timestamp: ' + str(self.time_stamp) + '\n'
        ret += '}'
        return ret



