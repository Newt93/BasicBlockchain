import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8') + self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        
    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        new_block = Block(data, previous_hash)
        self.chain.append(new_block)
        
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

bc = Blockchain()
bc.add_block("Hello")
bc.add_block("World")
print(bc.is_valid()) # should return True
