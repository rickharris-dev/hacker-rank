#!/usr/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    found = False
    try:
        for y in range(0, R - r + 1):
            for x in range(0, C - c + 1):
                if P[0][0] == G[y][x]:
                    try:
                        for row in range(0, r):
                            for col in range(0, c):
                                if P[row][col] != G[y + row][x + col]:
                                    raise
                        found = True
                    except:
                        pass
                if found:
                    raise
        print "NO"
    except:
        print "YES"
