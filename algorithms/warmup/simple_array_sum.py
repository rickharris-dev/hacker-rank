#!/usr/bin/python

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
total = 0
for item in arr:
    total += item

print total
