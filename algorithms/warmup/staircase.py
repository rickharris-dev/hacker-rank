#!/usr/bin/python

n = int(raw_input().strip())

for i in range(1,n + 1):
    line = ''
    for space in range(1,(n - i + 1)):
        line += ' '
    for step in range (1,i + 1):
        line += '#'
    print line
