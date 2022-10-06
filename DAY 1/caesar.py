plain = input("Enter a text: ")
key = int(input("How many shift? "))

def encrypt(p, k):
    cipher = ""
    for i in range(len(p)):
        char = p[i]
        if(char.isupper()):
            cipher += chr((ord(char) + k - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + k - 97) % 26 + 97)
    return cipher

def decrypt(c, k):
    plain = ""
    for i in range(len(c)):
        char = c[i]
        if(char.isupper()):
            plain += chr((ord(char) - k - 65) % 26 + 65)
        else:
            plain += chr((ord(char) - k -97) % 26 + 97)
    return plain

enc = encrypt(plain, key)
dec = decrypt(enc, key)

print(f"Original Text: {plain}", end="\n\n")
print(f"Cipher Text: {enc}")
print(f"De-Cipher Text: {dec}")