import hashlib
from datetime import datetime


#defining global variables
DIFFICULTY_LEVEL = 0
BLOCKCHAIN = []


class Block:
    def __init__(self, data, prev_hash="0"*64):
        self.blockId = len(BLOCKCHAIN)
        self.timestamp = datetime.now().strftime("%d-%h-%y  %H:%M:%S.%f")
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.hashBlock()

    def hashBlock(self):
        self.hash = hashlib.sha256((str(self.blockId) + str(self.data) + str(self.prev_hash) + str(self.nonce)).encode()).hexdigest()

        while self.hash[:DIFFICULTY_LEVEL] != "".zfill(DIFFICULTY_LEVEL):
            self.nonce += 1
            self.hash = hashlib.sha256((str(self.blockId) + str(self.data) + str(self.prev_hash) + str(self.nonce)).encode()).hexdigest()

        return self.hash


data = input("\nEnter the data: ")


#choose the difficulty leve for the Proof of Work
DIFFICULTY_LEVEL = int(input("\nEnter the difficulty level: "))


# blockchain is initialized and genesis block is created
block = Block(data)

BLOCKCHAIN.append(block)

print("\n", BLOCKCHAIN[-1].__dict__)

