import hackxercise6
import hackxercise7


def ex6():
    plaintext = b'Hello!          '
    k = b'1234567890123456'
    ciphertext = hackxercise6.aes_encrypt(plaintext, k)
    print(ciphertext)

    print(hackxercise6.aes_decrypt(ciphertext, k))


def ex7():
    s = "12345678901234567890123456789012345678901234567890"
    print(hackxercise7.is_english(s))


def main():
    ex7()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
