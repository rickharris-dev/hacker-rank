#!/usr/bin/python

t = int(raw_input().strip())
for i in range(0,t):
    s = raw_input().strip()
    if len(s) == 1:
        print 'no answer'
    else:
        # Sets variables
        new = ''

        # From end to start finds index where letters no longer increase
        for i in range(len(s) - 1,0,-1):
            if s[i] > s[i - 1]:
                break

        # Initializes new with the unaffected section of the string
        new = s[0:i - 1]

        # Creates sorted list of suffix letters
        check = sorted(s[i:])

        # Works through list to find the first letter larger than swap letter
        for c in range(0,len(check)):
            if check[c] > s[i - 1]:
                new = new + check[c]
                check[c] = s[i - 1]
                new = new + ''.join(check)
                break
        # If string length matches print string else print no answer
        if len(new) != len(s):
            print 'no answer'
        else:
            print new
