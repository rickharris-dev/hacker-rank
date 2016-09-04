#!/usr/bin/python

n,d = raw_input().strip().split(' ')
n,d = [int(n),int(d)]
a = map(int,raw_input().strip().split(' '))
beautiful = 0
for i in range(0, n - 2):
    aj = d + a[i]
    ak = (2 * d) + a[i]
    if aj in a[i + 1:n - 1]:
        j = a.index(aj)
        if ak in a[j + 1:n]:
            beautiful += 1
print beautiful
