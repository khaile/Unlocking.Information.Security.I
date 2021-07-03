from Crypto.Cipher import ARC4


def rc4(plaintext, key):
    return ARC4.new(key).encrypt(plaintext)
