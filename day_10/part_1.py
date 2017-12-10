#!/usr/bin/env python3

def rev(l, b, ln):
    subl = []
    for p in range(ln):
        subl.append(l[(b+p) % len(l)])
    p = b
    for i in reversed(subl):
        l[p] = i
        p = (p+1)%len(l)

items = list(range(256))
lens = [230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167]

pos = 0
skip = 0

for l in lens:
    rev(items, pos, l)
    pos = (pos + l + skip) % len(items)
    skip += 1

print(items[0] * items[1])
