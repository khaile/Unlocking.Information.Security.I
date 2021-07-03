# The function weak_md5 is a "weaker" version of MD5, using only the first 5 bytes of the MD5 hash.
# This means its hashing size is n = 40 and it can be brute forced rather easily.

# Implement a function find_collisions that loops over all the possible strings until it finds an arbitrary collision -
# that is, two different strings whose hash is the same - and returns them (as a tuple).

import hashlib
import itertools
import string


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    cache = {}
    product = list(itertools.product(string.ascii_uppercase, repeat=5))
    for chunk in product:
        origin = ''.join(chunk)
        checksum = weak_md5(origin.encode('latin-1'))

        if checksum in cache:
            return cache[checksum], origin

        cache[checksum] = origin


print(find_collisions())
