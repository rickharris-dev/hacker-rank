#!/usr/bin/python

n = raw_input()
a = map(int, raw_input().strip().split(' '))
largest = None

for v in sorted(a, reverse=True):
    if not largest:
        largest = v
    elif largest != v:
        print v
        break
