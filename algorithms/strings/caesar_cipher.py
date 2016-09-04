#!/usr/bin/python

n = int(raw_input().strip())
s = list(raw_input().strip())
k = int(raw_input().strip())

lower = range(97,123)
upper = range(65,91)

for i in range(0,len(s)):
    new = None
    if ord(s[i]) in lower:
        new = ord(s[i]) + k
        while(new - 97 > 25):
            new -= 26
    elif ord(s[i]) in upper:
        new = ord(s[i]) + k
        while(new - 65 > 25):
            new -= 26
    if new:
        s[i] = chr(new)
print ''.join(s)
