def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
    
def encrypt(string, key):
    cipher = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher.append(chr(x))
    return("" . join(cipher))

def decrypt(cipher_text, key):
    plain = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plain.append(chr(x))
    return("" . join(plain))
    

plain = input("Enter the text: ")
plain = plain.upper()
key = input("Enter the key: ")
key = generateKey(plain, key)
key = key.upper()
cipher = encrypt(plain,key)
print("Ciphertext : ", cipher)
print("Original/Decrypted Text: ",decrypt(cipher, key))