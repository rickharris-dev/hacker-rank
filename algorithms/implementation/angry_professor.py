#!/usr/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    count = 0
    for student in a:
        if student <= 0:
            count += 1
    if count < k:
        print "YES"
    else:
        print "NO"
