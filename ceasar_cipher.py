import string

ALPHABET = string.ascii_lowercase
ALPHABET_LENGTH = len(ALPHABET)


def ceasar_encrypt(plaintext, left_shift):
    output = []
    for c in plaintext:
        if c in ALPHABET:
            position = ALPHABET.index(c)
            shifted_position = (position - left_shift) % ALPHABET_LENGTH
            output.append(ALPHABET[shifted_position])
        else:
            output.append(c)

    return ''.join(output)


def ceasar_decrypt(ciphertext, left_shift):
    return ceasar_encrypt(ciphertext, -left_shift)


def ceasar_break(ciphertext):
    maybe = ''
    for index in range(1, ALPHABET_LENGTH):
        maybe = ceasar_decrypt(ciphertext, -index)
        print(maybe)

        for idx in range(1, ALPHABET_LENGTH):
            print(ceasar_decrypt(maybe, -idx))

    return maybe


msg = 'hello world'
encrypted_msg = "hm al, mo tmh hm al, huvh gn hul jzlnhgmt: qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo hul nxgtsn vty voomqn mr mzhovslmzn rmohztl, mo hm hvel vocn vsvgtnh v nlv mr homzaxln vty ak mppmngts lty hulc? hm ygl: hm nxllp; tm cmol; vty, ak v nxllp hm nvk ql lty hul ulvoh-vwul vty hul humznvty tvhzovx numwen huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt yldmzhxk hm al qgnu'y. hm ygl, hm nxllp; hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza; rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx, cznh sgdl zn pvznl"

print(ceasar_encrypt(msg, 2))
# print(ceasar_decrypt(encrypted_msg, 5))

ceasar_break(encrypted_msg)
