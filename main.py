import block
import blockchain

blchn = blockchain.Blockchain('testdata')
blchn.add_data('Testdata1')
blchn.add_data('Testdata2')
blchn.add_data('Testdata3')
print(blchn.validate_blockchain())
blchn.chain[1].this_hash = 'invalid'
print(blchn.validate_blockchain())
print(str(blchn))



