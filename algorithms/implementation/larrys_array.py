#!/usr/bin/python

t = int(raw_input().strip())
for i in range(0,t):
    n = int(raw_input().strip())
    a = map(int,raw_input().strip().split(' '))
    inversions = 0
    for j in range(0,n):
        inversions += abs(a[j] - (j + 1))
        while j > 0:
            if a[j - 1] > a[j]:
                swap = a[j]
                a[j] = a[j - 1]
                a[j - 1] = swap
                inversions -= 1
                j -= 1
            else:
                break
    if inversions % 2 == 0:
        print "YES"
    else:
        print "NO"
