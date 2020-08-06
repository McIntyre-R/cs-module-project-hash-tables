import random, re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
def Library(info): 
    info = re.sub('[^a-zA-Z0-9 \.\?\!]',' ',info)
    info = info.split()
    cache = {}
    for e in range(len(info)-1):
        if info[e] not in cache:
            cache[info[e]] = [info[e+1]]
        else:
            cache[info[e]].append(info[e+1])

    return cache


# TODO: construct 5 random sentences
# Your code here

def Construction(library, start):
    Sentence = [start]
    current = start
    while current in library:
        if current[-1:] in list('.?!'):
            break
        else:
            Sentence.append(random.choice(library[current]))
            current = Sentence[-1]
    return " ".join(Sentence)
L = Library(words)
K = list(L.keys())
for e in range(5):
    print(Construction(L,random.choice(K)))

