#!/usr/bin/python
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

alice = 0
bob = 0

for i in range(0,3):
    if a[i] > b[i]:
        alice = alice + 1
    elif b[i] > a[i]:
        bob = bob + 1

print alice, bob
