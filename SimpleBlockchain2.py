import hashlib
import datetime

blockchain = []

def getHash(blockId, nonce, data, timestamp, prevHash):
    while True:
        hash = hashlib.sha256((str(blockId) + str(nonce) + str(data) + str(timestamp) + str(prevHash)).encode()).hexdigest()
        if hash[:5] == "".zfill(5):
            break
        nonce += 1
    return hash, nonce

class Block:
    def __init__(self, data):
        self.blockId = blockchain[-1].blockId + 1
        self.nonce = 1
        self.data = data
        self.timestamp = datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S")
        self.prevHash = blockchain[-1].hash
        self.hash, self.nonce = getHash(self.blockId, self.nonce, self.data, self.timestamp, self.prevHash)

    def addBlock(self, data):
        blockchain.append(Block(data))

class Blockchain:
    def __init__(self):
        self.blockId = 0
        self.nonce = 1
        self.data = "Genesis Block"
        self.timestamp = datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S")
        self.prevHash = "0000"
        self.hash, self.nonce = getHash(self.blockId, self.nonce, self.data, self.timestamp, self.prevHash)

    def addBlock(self, data):
        blockchain.append(Block(data))

    

bc = Blockchain()

blockchain.append(bc)

bc.addBlock("this is 1st block")
bc.addBlock("this is 2nd block")

for i in blockchain:
    print(f"\n{i.__dict__}")