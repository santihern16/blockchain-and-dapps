from blockchain import Blockchain

class BlockchainUI:
    def __init__(self):
        self.blockchain = Blockchain()

    def run(self):
        print("Bloque genesis: ", self.blockchain.chain[0])
        self.blockchain.add_block("Segismundo envia 5 monedas a Rupertino")
        self.blockchain.add_block("Carlos envia 3 monedas a Ana")
        for block in self.blockchain.chain:
            print(block)
