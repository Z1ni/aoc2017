#!/usr/bin/env python3

stream = ""
with open("input.txt", "r") as f:
    stream = f.read().strip()

in_garbage = False
ignore = False
open_groups = 0
g_sum = 0
garbage_count = 0

for c in stream:
    if ignore:
        ignore = False
        continue
    if in_garbage:
        if c == "!":
            ignore = True
        elif c == ">":
            in_garbage = False
        else:
            garbage_count += 1
        continue
    if c == "<":
        in_garbage = True
        continue
    if c == "{":
        # Group start
        open_groups += 1
        g_sum += open_groups
    elif c == "}":
        # Group end
        open_groups -= 1

print("Score:", g_sum)
print("Garbage count:", garbage_count)