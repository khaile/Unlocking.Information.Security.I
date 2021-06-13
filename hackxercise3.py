def encrypt(plaintext, k):
    ciphertext = ''
    for idx in range(len(plaintext)):
        xored = ord(plaintext[idx]) ^ ord(k[idx])
        ciphertext += chr(xored)

    return ciphertext
