#!/usr/bin/python

t = int(raw_input().strip())
for i in range(0,t):
    str = raw_input().strip()
    deletions = 0
    for i in range(1,len(str)):
        if str[i] == str[i-1]:
            deletions = deletions + 1
    print deletions
