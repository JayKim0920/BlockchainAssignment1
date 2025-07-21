# Import required external modules
from cryptography.hazmat.primitives.asymmetric import rsa, padding
# RSA : module for public key cryptography
# Padding : provides padding template used for signatures.
from cryptography.hazmat.primitives import hashes, serialization
# Hashes : Provides Hashing functions such as SHA-256
# Serialization : converts keys to human-readable format(ex. PEM)

# Generate key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    #Generates a 2048 bit private key
public_key = private_key.public_key()
    #Extracts public key from private key.

# Serializes keys, enabling their transition to String.
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
).decode()
    #Private_bytes converts private keys into PEM Strings for humans to read
    #NoEncryption ensures the String will NOT be encrypted, as this script requires to view the key, not recommended in real practice.
    #.decode converts byets into plaintext.

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()
    #The same process is done for public key too.

print("Private Key:\n", private_pem)
print("Public Key:\n", public_pem)
    #Outpus plaintext keys

# Prompt to input message
message = input("Please enter a message to sign: ").encode()
    #Requires input to consider as a signable asset.

# Signature generation
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
    #private_key.sign signs the message with private key
    #Padding.PSS is the standart padding used in RSA signatures
    #MGF1 is a mask generation function that internally uses SHA-256. Salt_length used to determine length, maximum in this case.
    #hashes.SHA256() ensures usage of SHA-256 for hashing

print("Message:", message.decode())
print("Signature:", signature.hex())
    #prints input message and the signature. hex() is used to convert the signature from byte form to hexadecimal plaintext

# Validating signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except Exception as e:
    print("Signature is invalid.", e)
    #Public_key.verify validates the signature. The print result will notifies user with the result.