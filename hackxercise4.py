import os


def get_prg(plaintext_size, k):
    key_stream = ''
    i = j = 0
    k_chars = list(k)
    key_len = len(k)
    for idx in range(plaintext_size):
        i = (i + 1) % key_len
        j = (j + ord(k_chars[i])) % key_len

        k_chars[j], k_chars[i] = k_chars[i], k_chars[j]

        position = (ord(k_chars[i]) + ord(k_chars[j])) % key_len
        key_stream += k_chars[position]

    return key_stream


def fake_rc4(plaintext, keystream):
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(keystream[i]))

    return ciphertext
