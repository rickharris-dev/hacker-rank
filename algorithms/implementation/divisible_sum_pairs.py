#!/usr/bin/python
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
count = 0
i = 0

for i in range(0,n):
    j = i + 1
    while j < n:
        if (a[i] + a[j]) % k == 0:
            count += 1
        j += 1
print count
