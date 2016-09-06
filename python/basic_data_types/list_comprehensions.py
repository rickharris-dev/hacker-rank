#/usr/bin/python

x = int(raw_input().strip())
y = int(raw_input().strip())
z = int(raw_input().strip())
n = int(raw_input().strip())

print [[x, y, z] for x in range(x + 1) for y in range(y + 1) for z in range(z + 1) if x + y + z != n]
