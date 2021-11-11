import blockchain
import time
bl = blockchain.Block('apvs', 'testdata', time.time())
print(bl.mine_this_block())