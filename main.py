import asyncio

import blockchain
import computationnode


n0 = computationnode.ComputationNode("127.0.0.1", 8001, 'Testdata', 1)

n1 = computationnode.ComputationNode("127.0.0.1", 8002, 'Testdata', 2)
# Schedule three calls *concurrently*:

n0.start()
n1.start()

n0.connect_with_node('127.0.0.1', 8002)
n1.connect_with_node('127.0.0.1', 8001)

n0.send_to_node(2, 'Test')

n0.add_new_data('Testdata1')
n1.add_new_data('Testdata2')
n0.add_new_data('Testdata3')
n1.add_new_data('Testdata4')
n0.add_new_data('Testdata5')


print(str(n0.my_blockchain))
print(str(n1.my_blockchain))
# print(n0.my_blockchain.validate_blockchain())
# print(n1.my_blockchain.validate_blockchain())

n0.stop()
n1.stop()




