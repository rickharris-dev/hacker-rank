#!/usr/bin/python

t = int(raw_input().strip())
left = 0
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    chocolates = 0
    wrappers = 0
    bought = n / c
    chocolates += bought
    wrappers += bought
    while wrappers >= m:
        traded = wrappers / m
        wrappers = wrappers % m
        wrappers += traded
        chocolates += traded
    print chocolates
