#!/usr/bin/python

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
cloud = 0
jumps = 0
while cloud < n - 1:
    if cloud + 2 <= n - 1 and c[cloud + 2] != 1:
        cloud += 2
    else:
        cloud += 1
    jumps += 1
print jumps
