import hashlib

message = input("Enter a message: ")
hash = hashlib.md5(message.encode())

print("Equivalent hexadecimal message: ",hash.hexdigest())
print("Equivalent hash message: ",hash.digest())