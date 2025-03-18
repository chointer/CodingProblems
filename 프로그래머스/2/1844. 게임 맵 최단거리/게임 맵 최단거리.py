# maps (n, m) <= (100, 100), (1, 1)은 없음.
# '1' 따라 BFS. 완료되면 -1

import copy
from collections import deque
queue = deque()

def possible_moves(loc, maps, map_size):
    x_moves = (1, -1, 0, 0)
    y_moves = (0, 0, 1, -1)
    next_locs = []
    y, x = loc
    
    for dy, dx in zip(y_moves, x_moves):
        y_moved = y + dy
        x_moved = x + dx
        if y_moved >= 0 and y_moved < map_size[0] and x_moved >= 0 and x_moved < map_size[1] and maps[y_moved][x_moved] == 1:
            next_locs.append((y_moved, x_moved))
    return next_locs

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    
    st = (0, 0)
    goal = (h-1, w-1)
    queue.append((st[0], st[1], 1))     # y, x, distance
    maps[0][0] = 0
    
    while queue:
        y, x, d = queue.popleft()
        locs_candidate = possible_moves((y, x), maps, (h, w))
        for loc_candi in locs_candidate:
            if goal == loc_candi:
                return d + 1
            else:
                maps[loc_candi[0]][loc_candi[1]] = 0
                queue.append((loc_candi[0], loc_candi[1], d + 1))
        
    return -1