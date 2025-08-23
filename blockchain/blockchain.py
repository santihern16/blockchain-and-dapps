from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [Block(index=0, data='Genesis', previous_index=-1)]

    def add_block(self, data: str) -> Block:
        last = self.chain[-1]
        new_block = Block(index=last.index + 1, data=data, previous_index =last.index)
        self.chain.append(new_block)
        return new_block
