import asyncio

import blockchain
import node


async def main():
    l = []
    n0 = node.Node('Testdata', l)
    l.append(n0)
    n1 = node.Node('Testdata', l)
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        n0.add_new_data('Testdata1'),
        n1.add_new_data('Testdata2'),
        n0.add_new_data('Testdata3'),
        n1.add_new_data('Testdata4'),
        n0.add_new_data('Testdata5')
    )
    print(str(n0.my_blockchain))
    print(str(n1.my_blockchain))
    print(await n0.my_blockchain.validate_blockchain())
    print(await n1.my_blockchain.validate_blockchain())


asyncio.run(main())


