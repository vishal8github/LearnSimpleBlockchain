import hashlib
import datetime

class Block:
    def __init__(self, prevHash, data, timestamp):
        self.prevHash = prevHash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.getHash()

    def createGenesisBlock():
        return Block("0", "0", datetime.datetime.now())

    def getHash(self):
        header_bin = (str(self.prevHash) +
                      str(self.data) +
                      str(self.timestamp)).encode()
        
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        
        outer_hash = hashlib.sha256(inner_hash).hexdigest()

        return outer_hash


block_chain = [Block.createGenesisBlock()]

print("The genesis block has been created !")
print(f"Hash: {block_chain[-1].hash}")

num_blocks_to_add = 10

for i in range(1, num_blocks_to_add+1):
    block_chain.append(Block(block_chain[-1].hash, "DATA!", datetime.datetime.now()))

    print()

    print(f"Block #{i} has been created.")

    print(f"Block #{i} hash: {block_chain[i].hash}")