#!/usr/bin/python

def cycle(size, cycles, count):
    if cycles == count:
        return size
    if count % 2 == 0:
        size *= 2
    else:
        size += 1
    count += 1
    return cycle(size, cycles, count)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print cycle(1,n,0)
