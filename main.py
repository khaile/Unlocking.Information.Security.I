import string


def ceasar_cipher(plain_text, left_shift):
    alpha_string = string.ascii_lowercase

    output = []
    for c in plain_text:
        if c in alpha_string:
            position = alpha_string.index(c)
            shifted_position = (position - left_shift) % 26
            output.append(alpha_string[shifted_position])
        else:
            output.append(c)

    return ''.join(output)


def main():
    plain_text = 'hello world'
    print(ceasar_cipher(plain_text, 2))

    cipher_text = 'voovxf vo yvri'
    print(ceasar_cipher(cipher_text, -5))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
