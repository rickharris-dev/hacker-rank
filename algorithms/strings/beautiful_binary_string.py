#!/usr/bin/python

n = int(raw_input().strip())
B = list(raw_input().strip())
found = True
new = ''
moves = 0
while found:
    found = False
    if '01010' in ''.join(B):
        moves = moves + 1
        index = ''.join(B).index('01010')
        B[index + 2] = '1'
        found = True
found = True
while found:
    found = False
    if '010' in ''.join(B):
        moves = moves + 1
        index = ''.join(B).index('010')
        B[index + 1] = '0'
        found = True
print moves
