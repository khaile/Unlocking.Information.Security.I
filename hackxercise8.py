from hackxercise6 import aes_decrypt
from hackxercise7 import is_english

def brute_force_aes(ciphertext):
    for i in range(1000000):
        key = bytes('036' + str(i).zfill(6) + '0000000', 'utf-8')
        try:
            plaintext = aes_decrypt(ciphertext, key)
            if is_english(plaintext):
                return plaintext, key
        except UnicodeDecodeError:
            continue
