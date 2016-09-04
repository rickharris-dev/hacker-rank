#!/usr/bin/python
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0.0
neg = 0.0
zero = 0.0
div = float(len(arr))

for item in arr:
    if item > 0:
        pos += 1
    elif item < 0:
        neg += 1
    elif item == 0:
        zero += 1

print pos / div
print neg / div
print zero / div
