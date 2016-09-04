#!/usr/bin/python

def reduced_string(old_string):
    new_string = ''
    i = 0
    while (i < len(old_string)):
        if i == len(old_string) - 1:
            new_string = new_string + old_string[i]
        elif old_string[i] == old_string[i + 1]:
            i = i + 1
        else:
            new_string = new_string + old_string[i]
        i = i + 1
    return new_string

old_string = raw_input().strip()
new_string = None

while old_string != new_string:
    if new_string != None:
        old_string = new_string
    new_string = reduced_string(old_string)

if new_string:
    print new_string
else:
    print 'Empty String'
