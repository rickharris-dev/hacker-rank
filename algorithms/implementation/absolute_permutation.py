#!/usr/bin/python

t = int(raw_input().strip())
for i in range(0, t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    if k == 0:
        print ' '.join(str(x) for x in range(1, n + 1))
    elif n % (2 * k) != 0:
        print -1
    else:
        array = range(1, n + 1)
        i = 0
        while i < n:
            for j in range(0, k):
                array[i + j], array[i + j + k] = array[i + j + k], array[i + j]
            i += (k * 2)
        print ' '.join(str(x) for x in array)
