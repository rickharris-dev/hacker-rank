#!/usr/bin/python

n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = list(raw_input().strip())
    grid.append(grid_t)
cavities = []
for y in range(1,n):
    for x in range(1,n):
        try:
            if grid[y][x] <= grid[y - 1][x]:
                raise
            if grid[y][x] <= grid[y + 1][x]:
                raise
            if grid[y][x] <= grid[y][x - 1]:
                raise
            if grid[y][x] <= grid[y][x + 1]:
                raise
            cavities.append({'x': x, 'y': y})
        except:
            pass
for i in cavities:
    x = int(i['x'])
    y = i['y']
    grid[y][x] = 'X'
for i in grid:
    print ''.join(i)
