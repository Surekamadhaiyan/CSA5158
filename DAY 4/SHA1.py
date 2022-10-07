#import the module
import hashlib
#encode the message
text = hashlib.sha1(b'Hello')
#convert it to hexadecimal format
encrypt = text.hexdigest()
#print it
print(encrypt)