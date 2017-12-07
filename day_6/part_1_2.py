#!/usr/bin/env python3

mem = []
states = {}

with open("input.txt", "r") as f:
    mem = [int(i) for i in f.read().strip().split("\t")]

cnt = 0
while True:
    idx = mem.index(max(mem))
    val = mem[idx]

    mem[idx] = 0

    for i in range(val):
        mem[(idx + 1 + i) % len(mem)] += 1
        val -= 1

    tpl = tuple(mem)
    if states.get(tpl) is None:
        states[tpl] = cnt
        cnt += 1
    else:
        # Done
        print(len(states)+1)
        print(cnt - states[tpl])
        break
