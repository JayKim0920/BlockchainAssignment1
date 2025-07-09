# Imports required external modules
import hashlib # Module for Hash functions
import random # Module for random function
import string # Module to bring ASCII letters and digits

# Hashing function for SHA-256
# Encodes the given string s into bytes, then hashes it with SHA-256.
# Result is 16-bit string(hexdigest())
def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

# Displaying Avalanche Effect
def avalanche_effect(s):
    # Stores the hash value of the original string
    original_hash = hash_string(s)
    # Modifies just the first letter
    modified_s = s[:-1] + chr((ord(s[-1]) + 1) % 128) if s else 'a'
    modified_hash = hash_string(modified_s)

    print("\nOriginal String: ", s)
    print("Original Hash: ", original_hash)
    print("\nModified String: ", modified_s)
    print("Modified Hash: ", modified_hash)

    # Calculates the Hamming distance
    # Alters the two has values into 256bit binary, and compares each values to calculate hamming distance
    # Shows the avalance effect
    hamming_distance = sum(c1 != c2 for c1, c2 in zip(bin(int(original_hash, 16))[2:].zfill(256),
                                                      bin(int(modified_hash, 16))[2:].zfill(256)))
    print(f"\n🔷 Hamming Distance: {hamming_distance} bits out of 256")

# Attempt to find Pre-image
# Brute-forces random strings to find a match, has max attempts.
def preimage_attack(target_hash, max_attempts=10000):
    print(f"\n Trying to find pre-image for: {target_hash}")
    # Loops until match is found or reaches max attempts
    for attempt in range(1, max_attempts+1):
        # Creates random string to match target
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        guess_hash = hash_string(guess)
        if guess_hash == target_hash:
            print(f"Found pre-image: {guess} in {attempt} attempts")
            return
        if attempt % 1000 == 0:
            print(f"...{attempt} attempts so far...")
    print("Pre-image not found within attempt limit.")

# Main
if __name__ == "__main__":
    user_input = input("✍️ Enter a string: ")
    print("\n--- Avalanche Effect ---")
    avalanche_effect(user_input)

    target = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"  # SHA-256 for ("hello")
    print("\n--- Pre-image Attack ---")
    preimage_attack(target)