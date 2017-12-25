#!/usr/bin/env python3

import sys

map_data = None
with open(sys.argv[1], "r") as f:
    map_data = [list(l) for l in [l.strip("\n") for l in f.readlines()]]

# Vectors; up, left, down, right
vects = [(-1, 0), (0, -1), (1, 0), (0, 1)]

vect = (1, 0)   # Vector, down (Y, X)

# Get start point
y = 0
x = map_data[0].index('|')

width = len(map_data[0])
height = len(map_data)

letters = []
steps = 0

while True:
    c = map_data[y][x]
    if c == '|' or c == '-':
        # Vector is unchanged
        pass
    elif c == '+':
        # Vector should change
        choices = vects[:]
        try:
            # Try to remove the negation of the current vector
            choices.remove(tuple(map(lambda x: x * -1, vect)))
        except ValueError:
            pass
        for v in choices:
            c_y = y + v[0]
            c_x = x + v[1]
            if c_y < 0 or c_x < 0 or c_y >= height or c_x >= width:
                # Out of bounds
                continue
            c_c = map_data[c_y][c_x]
            if c_c != ' ':
                # Change vector
                vect = v
                break
    elif c == ' ':
        # End
        break
    else:
        # Letter
        letters.append(c)
    # Apply current vector
    y += vect[0]
    x += vect[1]
    steps += 1

print("Letters:", "".join(letters))
print("%d steps" % steps)