import string
import hashlib
from typing import TypeVar, Generic



T = TypeVar('T')

class Block(Generic[T]):
    thisHash: string
    prevHash: string
    data: T
    timestamp: int
    nonce = 0

    def calcThisHash(self):
        hashData = self.prevHash + str(self.data) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha3_256(hashData.encode('utf-8')).hexdigest()

    def __init__(self, prevHash: string, data: T, timestamp: int):
        self.prevHash = prevHash
        self.data = data
        self.timestamp = timestamp
        self.thisHash = self.calcThisHash()

        print(self.thisHash)
        print(self.prevHash)
        print(self.data)
        print(self.timestamp)



