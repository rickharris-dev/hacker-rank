#!/usr/bin/python

import string

s = raw_input().strip()
count = 0

if s:
    count = 1

for c in s:
    if c in string.uppercase:
        count = count + 1
print count
