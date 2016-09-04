#!/usr/bin/python
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
count = len(arr)
while count > 0:
    small = min(filter(None, arr))
    print count
    for i in range(0,len(arr)):
        if not isinstance(arr[i], int):
            pass
        elif arr[i] == small:
            arr[i] = None
        else:
            arr[i] -= small
    count = len(filter(None, arr))
