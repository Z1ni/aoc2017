#!/usr/bin/env python3

numstr = []
with open("input.txt", "r") as f:
    numstr = [l.strip().split() for l in f.readlines()]

diffs = []
for row in numstr:
    l = [int(i) for i in row]
    diffs.append(max(l) - min(l))

print(sum(diffs))
