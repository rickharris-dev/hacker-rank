#!/usr/bin/python

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

column = 0
p_diag = 0
s_diag = 0

'''Primary Diagonal'''
for i in a:
    p_diag += i[column]
    column += 1

'''Secondary Diagonal'''
for i in a:
    column -= 1
    s_diag += i[column]


print abs(p_diag - s_diag)
