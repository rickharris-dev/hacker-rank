#!/usr/bin/python

t = input()
list = []
for i in range(0,t):
    data = raw_input().strip().split(' ')
    if data[0] == 'insert':
        list.insert(int(data[1]), int(data[2]))
    elif data[0] == 'print':
        print list
    elif data[0] == 'remove':
        list.remove(int(data[1]))
    elif data[0] == 'append':
        list.append(int(data[1]))
    elif data[0] == 'sort':
        list = sorted(list)
    elif data[0] == 'pop':
        list.pop()
    elif data[0] == 'reverse':
        list = list[::-1]
