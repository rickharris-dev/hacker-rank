#!/usr/bin/python

s = raw_input().strip()
s = s.replace(' ', '').lower()
new = ''
for i in range(0,len(s)):
    if not s[i] in new:
        new = new + s[i]
if len(new) == 26:
    print 'pangram'
else:
    print 'not pangram'
