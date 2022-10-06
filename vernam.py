alphabets = dict((i, chr(i + 96)) for i in range(1, 27))

def generate_key(k):
    k = list(k)
    if(len(plain) == len(k)):
        return k
    else:
        for i in range(len(plain)- len(k)):
            k.append(k[i % len(k)])
    return("".join(k))

def encrypt(plain, key):
    plain = plain.lower()
    ckey = key
    cipher = ''
    for i in range(len(plain)):
        if plain[i] == ' ':
            cipher += ' '
        else:
            cipher += alphabets[(ord(plain[i]) + ord(ckey[i])) % 26]
    return("".join(cipher))

plain = "HELLO"
key = "HI"
key = generate_key(key)
enc = encrypt(plain, key)
print(enc)