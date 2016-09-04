#!/usr/bin/python

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
energy = 100
cloud = None
while cloud != 0:
    if cloud == None:
        cloud = 0
    cloud += k
    if cloud > n - 1:
        cloud -= n
    energy -= (1 + (c[cloud] * 2))
print energy
