#!/usr/bin/python

import sys

a = int(raw_input().strip())
b = int(raw_input().strip())

sys.stdout.write(	str(a + b) + '\n'
					+ str(a - b) + '\n'
					+ str(a * b) + '\n')
