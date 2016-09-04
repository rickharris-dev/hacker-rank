#!/usr/bin/python

N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

odd_loaves = []
total_loaves = 0

for i in range(0, N):
    if B[i] % 2 == 1:
        odd_loaves.append(i)
if len(odd_loaves) % 2 == 1:
    print "NO"
else:
    even = []
    odd = []
    for i in range(0, len(odd_loaves) - 1):
        if i % 2 == 0:
            difference = odd_loaves[i + 1] - odd_loaves[i]
            even.append(difference)
    total_loaves = sum(even) * 2
    print total_loaves
