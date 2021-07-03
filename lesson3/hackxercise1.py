from hashlib import md5, sha1, sha256, sha3_256

message = b"Hello, world!"
print(md5(message).hexdigest())
print(sha1(message).hexdigest())
print(sha256(message).hexdigest())
print(sha3_256(message).hexdigest())
