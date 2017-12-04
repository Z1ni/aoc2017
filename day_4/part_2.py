#!/usr/bin/env python3

def is_correct(phrase):
    words = phrase.split()
    for i, word in enumerate(words):
        for e, word2 in enumerate(words):
            if i == e:
                continue
            if sorted(word) == sorted(word2):
                return False
    return True

with open("input.txt", "r") as f:
    print(sum(map(is_correct, [l.strip() for l in f.readlines()])))
