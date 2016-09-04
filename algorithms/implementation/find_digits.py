#!/usr/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n_str = str(n)
    even = 0
    for c in n_str:
        if c != '0' and n % int(c) == 0:
            even += 1
    print even
