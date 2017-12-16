#!/usr/bin/env python3

a = 65
b = 8921

same = 0
for i in range(40000000):
    if i % 100000 == 0:
        print(i)
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if (a & 0xFFFF) == (b & 0xFFFF):
        same += 1
print(same)
