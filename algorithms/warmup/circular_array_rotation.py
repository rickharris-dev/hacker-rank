#!/usr/bin/python
n, k, q = raw_input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
arr = map(int,raw_input().strip().split(' '))

for case in range(0,q):
    p = int(raw_input().strip())
    e = k % n
    i = (p - e) % n
    print arr[i]
