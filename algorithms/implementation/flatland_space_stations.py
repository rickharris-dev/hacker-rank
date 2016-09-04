#!/usr/bin/python

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))
max = 0
if len(c) == n:
    print 0
else:
    for i in range(0,len(c)):
        if i != 0:
            j = i
            while j > 0 and c[j] < c[j - 1]:
                c[j], c[j-1] = c[j-1], c[j]
                j -= 1
    for i in range(0, len(c) - 1):
        if ((c[i + 1] - c[i]) / 2) > max:
            max = ((c[i + 1] - c[i]) / 2)
    if (n - 1) - c[len(c) - 1] > max:
        max = (n - 1) - c[len(c) - 1]
    if c[0] > max:
        max = c[0]
    print max
