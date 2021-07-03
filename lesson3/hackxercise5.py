# To see how hard it is to brute force a real hash function, try running the function you wrote in the previous ex,
# but using the full MD5. My guess is, your code will return in a few thousand years...

import hashlib
import itertools
import string


def real_md5(s):
    return hashlib.md5(s).digest()


def find_collisions():
    cache = {}
    product = list(itertools.product(string.ascii_uppercase, repeat=5))
    for chunk in product:
        origin = ''.join(chunk)
        checksum = real_md5(origin.encode('latin-1'))

        if checksum in cache:
            return cache[checksum], origin

        cache[checksum] = origin


print(find_collisions())
