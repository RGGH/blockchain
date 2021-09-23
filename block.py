# node/block.py
class Block(object):
    def __init__(self, previous_block=None):
        self.previous_block = previous_block
# Example
block_0 = Block()
block_1 = Block(previous_block=block_0)
block_2 = Block(previous_block=block_1)

print(block_2)