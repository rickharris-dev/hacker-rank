#!/usr/bin/python

n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
min_dist = None
for i in range(0,n):
    try:
        dist = A[i+1:n].index(A[i]) + 1
        if not min_dist or min_dist > dist:
            min_dist = dist
    except:
        pass
if not min_dist:
    print -1
else:
    print min_dist
