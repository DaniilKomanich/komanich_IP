#!/usr/bin/env python

def hash_func(num):
    a = num
    a = (a ^ 11) + (a << 16)
    a ^= (a >> 10)
    a += (a ** 7)
    a ^= (a << 44)
    return a

hashes = {}
test_count = 100000
collisions = []
for num in range(test_count):
    hash = hash_func(num)
    if hash in hashes:
        collisions.append([num, hashes[hash], hash])
    hashes[hash] = num

if len(collisions) == 0:
  print("There is no collisions for a hash function")

else:
  print(f"Found {len(collisions)} collisions for a hash function - {len(collisions) / test_count:3.3%}")
  for i in range(min(1000, len(collisions))):
    c = collisions[i]
    print(f"hash({c[0]}) ==  hash({c[1]}) = {c[2]}")