#!/usr/bin/python

import string

s = int(raw_input().strip())
gems = {}
total = 0
for i in range(0,s):
    string = raw_input().strip()
    unique = []
    for c in string:
        if not c in unique:
            unique.append(c)
            if c in gems.keys():
                gems[c] = gems[c] + 1
            else:
                gems[c] = 1
for key in gems:
    if gems[key] == s:
        total = total + 1
print total
