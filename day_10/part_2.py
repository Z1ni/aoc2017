#!/usr/bin/env python3

def rev(l, b, ln):
    subl = []
    for p in range(ln):
        subl.append(l[(b+p) % len(l)])
    p = b
    for i in reversed(subl):
        l[p] = i
        p = (p+1)%len(l)

inp = "230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167"
lens = [ord(c) for c in inp] + [17, 31, 73, 47, 23]

items = list(range(256))

pos = 0
skip = 0

for r in range(64):
    for l in lens:
        rev(items, pos, l)
        pos = (pos + l + skip) % len(items)
        skip += 1

# From sparse to dense hash
p = 0
xors = []
for i in range(16):
    xor = 0
    for x in items[p:p+16]:
        xor ^= x
    xors.append(xor)
    p += 16

print("".join(map(lambda x: "{0:02x}".format(x), xors)))
