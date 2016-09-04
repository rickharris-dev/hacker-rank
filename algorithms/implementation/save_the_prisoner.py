#!/usr/bin/python

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

for case in a:
    prisoners = case[0]
    sweets = case[1]
    target = case[2]

    pos = (sweets % prisoners) - 1
    target += pos
    if target > prisoners:
        target -= prisoners
    if target == 0:
        target = prisoners
    print target
