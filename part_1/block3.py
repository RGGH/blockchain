'''A blockchain is a growing list of records, called blocks, that are linked together using
cryptography. Each block contains a cryptographic hash of the previous block, a
timestamp, and transaction data.'''

# hashes in the bitcoin are protocol typically computed twice
import hashlib
d = hashlib.sha256(b"hello")
d2 = hashlib.sha256()
d.hexdigest()
d2.update(d.digest())
d2.hexdigest()
print(d2.digest())

# https://en.bitcoin.it/wiki/Protocol_documentation#Hashes
# https://en.bitcoin.it/wiki/Network
# https://en.bitcoin.it/wiki/Help:FAQ#What_is_Bitcoin.3F

# Why are hashes in the bitcoin protocol typically computed twice (double computed)?
# https://en.wikipedia.org/wiki/Length_extension_attack
# https://ctftime.org/writeup/30223


from datetime import datetime
timestamp_0 = datetime.timestamp(datetime.fromisoformat('2011-11-04 00:05:23.111'))


'''You have to be careful what you mean by "string". 
A string is a sequence of characters, while hash function usually process byte sequences. 
If you use different encodings to map strings to byte sequences this can give you different hashvalues'''
