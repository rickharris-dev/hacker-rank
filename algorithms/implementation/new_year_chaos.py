#!/usr/bin/python

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    bribes = 0
    chaos = False
    sort = False
    while not sort and not chaos:
        sort = True
        for i in range(0,n-1):
            if q[i] > q[i + 1]:
                sort = False
                if q[i] - (i + 1) > 2:
                    chaos = True
                    break
                q[i], q[i + 1] = q[i + 1], q[i]
                bribes += 1
    if chaos:
        print "Too chaotic"
    else:
        print bribes
