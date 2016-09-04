#!/usr/bin/python

from math import *

t = int(raw_input().strip())
for case in range(0,int(t)):
    low,high = raw_input().strip().split(' ')
    low,high = [int(low), int(high)]
    squares = 0
    for i in range(int(sqrt(low)), int(sqrt(high)) + 1):
        if i**2 >= low and i**2 <= high:
            squares += 1
        elif i**2 > high:
            break
    print squares
