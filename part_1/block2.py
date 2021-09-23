# block2.py
# https://www.browserling.com/tools/random-bytes
# https://www.machinelearningplus.com/python/python-property/

import json
from datetime import datetime

from Crypto.Hash import SHA256
def calculate_hash(data: bytes) -> str:
    h = SHA256.new()
    h.update(data)
    return h.hexdigest()

class Block:
    def __init__(self,timestamp: float, transaction_data:str, previous_block=None,):
        self.transaction_data = transaction_data
        self.timestamp = timestamp
        self.previous_block = previous_block

    @property
    def previous_block_cryptographic_hash(self):
        previous_block_cryptographic_hash = ""
        if self.previous_block:
            previous_block_cryptographic_hash = self.previous_block.cryptographic_hash
        return previous_block_cryptographic_hash

    @property
    def cryptographic_hash(self) -> str:
        block_content = {
        "transaction_data": self.transaction_data, 
        "timestamp": self.timestamp, 
        "previous_block_cryptographic_hash": self.previous_block_cryptographic_hash
        }
        block_content_bytes = json.dumps(block_content, indent=2).encode('utf-8')
        return calculate_hash(block_content_bytes)
        
# inputs
timestamp_0 = datetime.timestamp(datetime.fromisoformat('2011-11-04 00:05:23.111'))
transaction_data_0 = "Albert,Bertrand,30"
block_0 = Block(
transaction_data=transaction_data_0,
timestamp=timestamp_0
)
timestamp_1 = datetime.timestamp(datetime.fromisoformat('2011-11-07 00:05:13.222'))
transaction_data_1 = "Albert,Camille,10"
block_1 = Block(
transaction_data=transaction_data_1,
timestamp=timestamp_1,
previous_block=block_0
)
timestamp_2 = datetime.timestamp(datetime.fromisoformat('2011-11-09 00:11:13.333'))
transaction_data_2 = "Bertrand,Camille,5"
block_2 = Block(
transaction_data=transaction_data_2,
timestamp=timestamp_2,
previous_block=block_1
)

# main 
b2 = Block(timestamp_2,transaction_data_2, block_2)

print(b2.previous_block_cryptographic_hash)
print(b2.transaction_data)