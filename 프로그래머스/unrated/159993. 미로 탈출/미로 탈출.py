# BFS 2 times
from collections import deque
from copy import deepcopy

def BFS(st, en, maps, visits):
    dX = [0, 0, 1, -1]   # Up, Down, Right, Left
    dY = [1, -1, 0, 0]
    X = len(maps[0])
    Y = len(maps)
    visits[st[0]][st[1]] = True
    steps = deque([st])
    
    while steps:
        y, x, n = steps.popleft()
        for dy, dx in zip(dY, dX):
            y_next, x_next = y + dy, x + dx
            if y_next >= 0 and y_next < Y and x_next >= 0 and x_next < X:
                if y_next == en[0] and x_next == en[1]:
                    return n + 1
                if visits[y_next][x_next] is False:
                    steps.append((y_next, x_next, n + 1))
                    visits[y_next][x_next] = True
    
    return -1
                
        
    
    
    
def solution(maps):
    # Find S, L, E, make visits
    visits = []
    for y, m in enumerate(maps):
        vis = []
        for x, val in enumerate(m):
            if val == 'X':
                vis.append(True)
            else:
                vis.append(False)
                
            if val == 'S':
                S = (y, x, 0)
            elif val == 'L':
                L = (y, x, 0)
            elif val == 'E':
                E = (y, x, 0)
        visits.append(vis)
    
    SL = BFS(S, L, maps, deepcopy(visits))
    LE = BFS(L, E, maps, deepcopy(visits))
    
    return SL + LE if SL > 0 and LE > 0 else -1