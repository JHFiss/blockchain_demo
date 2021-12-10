import asyncio
import blockchain
from typing import TypeVar, Generic

T = TypeVar('T')


class Node:
    """
    Class that represents a Computing Node
    """
    my_blockchain: blockchain
    nodelist: list

    async def add_new_data(self, data: Generic[T]):
        """
        Add new Data to the Blockchain of this Node
        :param data: Generic[T] data that is added to the blockchain
        :return: nothing
        """
        await self.my_blockchain.add_data(data)
        for n in self.nodelist:
            await n.validate_and_update_blockchain(self.my_blockchain)

    async def validate_and_update_blockchain(self, bc: blockchain):
        """
        Checks if the blockchain of this node is equal or longer to a given blockchain,
        if not, it is replaced with the newly arrived blockchain
        :param bc: blockchain the blockchain this node's blockchain is compared to
        :return:
        """
        await bc.validate_blockchain()
        if not await self.my_blockchain.compare_to(bc):
            self.my_blockchain = bc

    def __init__(self, data: Generic[T], other_nodes=[]):
        self.my_blockchain = blockchain.Blockchain(data)
        self.nodelist = other_nodes
        print(list)
        self.nodelist.append(self)
