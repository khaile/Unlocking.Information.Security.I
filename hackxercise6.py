from Crypto.Cipher import AES
from Crypto import Random


def aes_encrypt(plaintext, k):
    iv = Random.new().read(16)
    cipher = AES.new(k, AES.MODE_CBC, iv)

    return iv + cipher.encrypt(plaintext)


def aes_decrypt(ciphertext, k):
    iv = ciphertext[:16]
    cipher = AES.new(k, AES.MODE_CBC, iv)

    return cipher.decrypt(ciphertext[16:]).decode('latin-1')
