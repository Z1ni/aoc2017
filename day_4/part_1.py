#!/usr/bin/env python3

with open("input.txt", "r") as f:
    passphrases = [l.strip() for l in f.readlines()]

valid = 0
for phrase in passphrases:
    split = phrase.split()
    if len(set(split)) == len(split):
        valid += 1
print(valid)
