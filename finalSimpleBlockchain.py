import hashlib
from datetime import datetime


#defining global variables
DIFFICULTY_LEVEL = 0
BLOCKCHAIN = []


class Block:
    def __init__(self, data, prev_hash=None):
        self.blockId = len(BLOCKCHAIN)
        self.timestamp = datetime.now().strftime("%d-%h-%y  %H:%M:%S.%f")
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.hashBlock()

    def hashBlock(self):
        data = (str(self.blockId) + str(self.data) + str(self.prev_hash) + str(self.nonce)).encode()
        return hashlib.sha256(data).hexdigest()


class Chain:
    def __init__(self):
        self.addBlock("Genesis Block")

    def addBlock(self, data):
        if len(BLOCKCHAIN) == 0:
            prev_hash = "0"*64
            newBlock = Block(data, prev_hash)

            newBlock.hash = self.proofOfWork(newBlock)

            BLOCKCHAIN.append(newBlock)
        else:
            prev_hash = BLOCKCHAIN[-1].hash
            newBlock = Block(data, prev_hash)
            
            newBlock.hash = self.proofOfWork(newBlock)

            BLOCKCHAIN.append(newBlock)

    def getChain(self):
        return BLOCKCHAIN

    def proofOfWork(self, block):
        while block.hash[:DIFFICULTY_LEVEL] != "".zfill(DIFFICULTY_LEVEL):
            block.nonce += 1
            block.hash = block.hashBlock()
        return block.hash

    def isValid(self):
        for i in range(1, len(BLOCKCHAIN)):
            curntBlock = BLOCKCHAIN[i]
            prevBlock = BLOCKCHAIN[i-1]

            if curntBlock.hash != curntBlock.hashBlock():
                return False
            if curntBlock.prev_hash != prevBlock.hash:
                return False
        return True




numOfBlocks = int(input("\nHow many blocks do you want to create: "))


#choose the difficulty leve for the Proof of Work
DIFFICULTY_LEVEL = int(input("\nEnter the difficulty level: "))


# blockchain is initialized and genesis block is created
blockchain = Chain()
print("\n", BLOCKCHAIN[-1].__dict__)


for num in range(1, numOfBlocks):
    blockchain.addBlock(f"New Block {num}")
    print("\n", BLOCKCHAIN[-1].__dict__)



print(f"\n\nBlockchain is valid: {blockchain.isValid()}")
