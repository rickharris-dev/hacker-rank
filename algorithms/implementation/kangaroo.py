#!/usr/bin/python
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

same = False

while (x1 != x2):
    if v1 > v2 and x1 > x2:
        break
    elif v2 > v1 and x2 > x1:
        break
    elif v1 == v2 and x1 != x2:
        break
    x1 += v1
    x2 += v2

if x1 == x2:
    print "YES"
else:
    print "NO"
