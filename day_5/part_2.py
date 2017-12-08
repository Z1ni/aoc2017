#!/usr/bin/env python3

offsets = []
with open("input.txt", "r") as f:
    offsets = [int(l.strip()) for l in f.readlines()]

pos = 0
steps = 0
while True:
    jmp = offsets[pos]
    amt = 1
    if jmp >= 3:
    	amt = -1
    offsets[pos] += amt
    pos += jmp
    steps += 1
    if pos < 0 or pos >= len(offsets):
        break

print(steps)