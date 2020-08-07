# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import re
# Your code here
with open("ciphertext.txt") as f:
    cipher = f.read()
common = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
def crack(ciph):
    cache = {}
    ciph = re.sub('[^a-zA-Z]','',ciph)

    for e in ciph:
        if e in cache:
            cache[e] += 1
        else:
            cache[e] = 1
    key = sorted(cache.items(), key=lambda x: x[1], reverse=True)
    for e in range(len(key)):
        key[e] = key[e][0]
    return key
code = dict(zip(crack(cipher), common))
print(cipher.translate(str.maketrans(code)))
    
