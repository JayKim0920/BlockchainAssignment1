# hashlib is used to use the hashing algorithms, and time is used to give delays between blocks.
import hashlib
import time

# Defines a new class 'Block'
class Block:
    def __init__(self, block_id, data, previous_hash, nonce=0):
        self.block_id = block_id # Block's id
        self.timestamp = time.time() # Timestamp of the block creation time
        self.data = data # Data to be stored in the block
        self.previous_hash = previous_hash # Hash of the previous block
        self.nonce = nonce # Set to default value 0
        self.hash = self.calculate_hash()

    # Combines the key values of the block into a string and encodes them into byte forms, and returns the 16-bit SHA256 hash value.
    # This hash acts as the fingerprint of the block
    def calculate_hash(self):
        block_string = f"{self.block_id}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Formats the output for readability
    def __str__(self):
        return (f"Block ID: {self.block_id}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Nonce: {self.nonce}\n"
                f"Hash: {self.hash}\n")

# Blockchain Generation
# Initializes chain and previous hash value
chain = [] # A list(chain) to contain the blocks
previous_hash = "0" # The genesis block(first block) does not have a previous hash, so it is set to 0.

for i in range(5):  # Five blocks to be made
    data = f"Dummy data for block {i}"
    block = Block(i, data, previous_hash)
    chain.append(block)
    print(block)
    previous_hash = block.hash
    time.sleep(1)  # A delay to show step by step generations of blocks

# Notifies the completion of generation
print("Blockchain simulation complete.")