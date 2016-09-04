#!/usr/bin/python

class Node(object):

    def __init__(self, deadline = 0, minutes = 0, next_node = None):
        self.deadline = deadline
        self.minutes = minutes
        self.next_node = next_node

    def set_next(self, next_node):
        self.next_node = next_node

first = None
wc = 0
wc_deadline = 0
wc_minutes = 0

t = int(raw_input().strip())
for i in range(0, t):
    d, m = raw_input().strip().split(' ')
    d, m = [int(d), int(m)]
    pointer = first
    previous = None
    check = 0

    if d <= wc_deadline:
        wc = wc + m
        wc_minutes = wc_minutes + m
        pointer = first
    else:
        while pointer and pointer.deadline <= d:
            check = check + pointer.minutes
            previous = pointer
            pointer = pointer.next_node

        if pointer is first:
            first = Node(d, m)
            first.next_node = pointer
            pointer = first
        else:
            new = Node(d, m)
            previous.next_node = new
            new.next_node = pointer
            pointer = new

    while pointer:
            check = check + pointer.minutes
            if wc_minutes + check - pointer.deadline > wc:
                wc = wc_minutes + check - pointer.deadline
                wc_minutes = wc_minutes + check
                wc_deadline = pointer.deadline
                first = pointer.next_node
                check = 0
            pointer = pointer.next_node
    print wc
