import hashlib

key = open('input.txt').readlines()[0]

num = -1
hash = None
while hash is None or hash[:6] != '000000':
    num += 1
    string_to_hash = key + str(num)
    res = hashlib.md5(string_to_hash.encode())
    hash = res.hexdigest()
print(hash)
print(num)