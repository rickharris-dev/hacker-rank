#!/usr/bin/python

t = int(raw_input().strip())
for i in range(0,t):
    possibilities = []
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    for c in range(0, n):
        last = (b * c) + (a * (n - c -1))
        if not last in possibilities:
            if b > a:
                possibilities.append(last)
            if a >= b:
                possibilities.insert(0,last)
    print ' '.join(str(x) for x in possibilities)
