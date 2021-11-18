import block
import time
bl = block.Block('apvs', 'testdata', time.time())
print(bl.mine_this_block())
l = [bl]
for x in range(1, 5):
    prev_hash = l.__getitem__(x-1).this_hash
    data = 'testdata' + str(x)
    next_block = block.Block(prev_hash, data, time.time())
    next_block.mine_this_block()
    l.append(next_block)

for x in range(0, 5):
    print(str(l.__getitem__(x)))


