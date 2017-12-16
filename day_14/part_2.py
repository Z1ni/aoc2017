#!/usr/bin/env python3

import struct

grid = []
regions = 0

def rev(l, b, ln):
    subl = []
    for p in range(ln):
        subl.append(l[(b+p) % len(l)])
    p = b
    for i in reversed(subl):
        l[p] = i
        p = (p+1)%len(l)

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

def conquer(y, x, lvl=0):
    global grid
    global regions
    grid[y][x] = regions
    # Check nearby
    check = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for n in check:
        ny = y+n[0]
        nx = x+n[1]
        if ny < 0 or nx < 0 or ny >= 128 or nx >= 128:
            continue
        if grid[ny][nx] == '#':
            conquer(ny, nx, lvl+1)

key = "stpzcrnm"

# Generate grid
"""
for i in range(128):
    hsh = knot_hash("%s-%d" % (key, i))
    row = ""
    for b in hsh:
        row += format(b, "08b").replace("0", ".").replace("1", "#")
    print(row)
"""

# Read grid
with open("grid.txt", "r") as f:
    grid = [list(l.strip()) for l in f.readlines()]

regions = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '#':
            conquer(y, x)
            regions += 1

for row in grid:
    for col in row:
        if col == '.':
            print("\033[38;5;234m\u2588\033[0m", end="")
            continue
        c = (col + 21) % 231 # (col % 0xE7) - 0x10
        #print("\033[%dm" % (31+c), end="")
        print("\033[38;5;%dm" % c, end="")
        #print(str(col)[-1], end="\033[0m")
        print("\u2588", end="\033[0m")
    print()

print(regions)
