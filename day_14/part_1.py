#!/usr/bin/env python3

import struct
import math

def rev(l, b, ln):
    subl = []
    for p in range(ln):
        subl.append(l[(b+p) % len(l)])
    p = b
    for i in reversed(subl):
        l[p] = i
        p = (p+1)%len(l)

def popcount(d):
    s = 0
    for n in struct.unpack('Q'*(len(d)//8), d):
        n -= (n >> 1) & 0x5555555555555555
        n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
        n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
        s += ((n * 0x0101010101010101) & 0xffffffffffffffff ) >> 56
    return s

def knot_hash(inp):
    lens = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
    items = list(range(256))
    pos = 0
    skip = 0
    for r in range(64):
        for l in lens:
            rev(items, pos, l)
            pos = (pos + l + skip) % len(items)
            skip += 1
    p = 0
    xors = []
    for i in range(16):
        xor = 0
        for x in items[p:p+16]:
            xor ^= x
        xors.append(xor)
        p += 16
    return bytes(xors)

key = "stpzcrnm"

sq_used = 0
prog = 0
print("[                                                  ]", end="\r")
for i in range(128):
    hsh = knot_hash("%s-%d" % (key, i))
    sq_used += popcount(hsh)
    prog = ((i+1) / 128 * 100)
    print("[", end="")
    print("#"*math.ceil(prog / 2), end="")
    left = math.ceil(50 - (prog / 2))
    print(" "*(left-1) + "] %.2f %%" % prog, end="\r")
print()
print(sq_used)
