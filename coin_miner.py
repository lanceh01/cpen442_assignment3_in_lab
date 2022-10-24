import hashlib
import requests
import base64
import time

def check_hash(hash, num_zero):
    return hash[0:num_zero] == "0" * num_zero

start = time.time()
hash_of_preceding_coin = b"a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
id_of_miner = b"free-vbucks"
num_zeros = 7

found = False

# push keys into this dict
return_key = {}

num = 0

while not found:
    coin_blob = num.to_bytes(64,"little")
    to_hash = b"CPEN 442 Coin" + b"2022" + hash_of_preceding_coin + coin_blob + id_of_miner
    h = hashlib.sha256(to_hash).hexdigest()
    if (check_hash(h, num_zeros)):
        found = True
        break
    num += 1

print(time.time()-start)
print(h)
print(base64.b64encode(coin_blob))
print(num)
print(num_zeros)
    