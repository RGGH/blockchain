from Crypto.Hash import SHA256
def calculate_hash(data: bytes) -> str:
    h = SHA256.new()
    h.update(data)
    return h.hexdigest()

print(calculate_hash(b'helllo'))

'''
SHA-256 cryptographic hash algorithm.

SHA-256 belongs to the SHA-2_ family of cryptographic hashes. 
It produces the 256 bit digest of a message.

>>> from Crypto.Hash import SHA256
>>>
>>> h = SHA256.new()
>>> h.update(b'Hello')
>>> print h.hexdigest()
*SHA* stands for Secure Hash Algorithm.
'''