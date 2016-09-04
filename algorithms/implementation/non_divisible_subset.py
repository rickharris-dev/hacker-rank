#!/usr/bin/python
import operator

n, k = raw_input().strip().split(" ")
n, k = [int(n), int(k)]
array = raw_input().strip().split(" ")
mod_dict = {}
for num in array:
    mod = int(num) % k
    if not mod in mod_dict:
        mod_dict[mod] = 0
    mod_dict[mod] += 1
for i in range(0, (k / 2) + 1):
    if i in mod_dict:
        if i == 0:
            mod_dict[i] = 1
        elif k - i == i:
            mod_dict[k / 2] = 1
        elif (k - i) in mod_dict:
            if mod_dict[i] < mod_dict[k - i]:
                del mod_dict[i]
            else:
                del mod_dict[k - i]
total = 0
for k in mod_dict:
    total += mod_dict[k]
print total
