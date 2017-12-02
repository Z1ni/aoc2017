#!/usr/bin/env python3

numstr = []
with open("input.txt", "r") as f:
    numstr = [l.strip().split() for l in f.readlines()]

div = []
for row in numstr:
    l = [int(i) for i in row]
    ok = False
    for n1 in l:
        for n2 in l:
            if n1 == n2:
                continue
            d = n1 / n2
            if d.is_integer():
                div.append(n1 // n2)
                ok = True
                break
        if ok:
            break

print(sum(div))
