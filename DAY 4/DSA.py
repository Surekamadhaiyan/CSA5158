from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

key_size = 1024
message = "Hello".encode()
key = DSA.generate(key_size)

publickey = key.publickey()
print(publickey.exportKey())

message_hash = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(message_hash)
print(int.from_bytes(signature, "big", signed=False))

verifier = DSS.new(publickey, 'fips-186-3')

try:
    verifier.verify(message_hash, signature)
    print("Verification Successful")
except ValueError:
    print("Verification Failed")

    