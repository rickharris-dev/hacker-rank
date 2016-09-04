#!/usr/bin/python
import math

t = int(raw_input().strip())

mod = t % 3
log = int(math.log((t + 2)/3,2))
rem = ((t + 2)/3) - (2**log)
if mod == 0:
    mod = 3
value = (3 * (2 ** log))
position = ((3 * rem) + (mod - 1))
print value - position
