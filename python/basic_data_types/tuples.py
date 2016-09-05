#!/usr/bin/python

i = raw_input()
t = map(int, raw_input().strip().split(' '))
t = tuple(t)
print hash(t)
