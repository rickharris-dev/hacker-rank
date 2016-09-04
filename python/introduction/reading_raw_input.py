#!/usr/bin/python

while raw_input:
    try:
        print raw_input().strip()
    except EOFError:
        break
