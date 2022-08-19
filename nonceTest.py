import hashlib

data = "hello world"

nonce = 1

while True:
    hash = (data + str(nonce)).encode()
    hash = hashlib.sha256(hash).hexdigest()
    
    print(hash,"\n")

    if hash[:3] == "".zfill(3):
        break
    nonce += 1

print(f"\nhash: {hash}")
print(f"\nnonce: {nonce}")