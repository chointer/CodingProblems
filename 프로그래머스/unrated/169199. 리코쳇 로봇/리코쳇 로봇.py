# BFS? Dijkstra?
# 1. find direction, BFS
# 2. move
# 3. compare; if N_now >= N_min: -> 2. // N_now < N_min: record.
# 4. check if the position is the Goal. else: -> 1.
# ! inefficiency: recalculations for visited directions.

#from collections import deque
import heapq

def find_nexts(Nmove, x, y, todos, board, NX, NY):
    xmoves = [1, -1, 0, 0]
    ymoves = [0, 0, 1, -1]
    
    for dx, dy in zip(xmoves, ymoves):
        nx = x + dx
        ny = y + dy
        
        while nx >= 0 and nx < NX and ny >= 0 and ny < NY and board[ny][nx] != 'D':
            nx += dx
            ny += dy
        if not ((nx == x + dx) and (ny == y + dy)):
            heapq.heappush(todos, (Nmove, nx - dx, ny - dy))
    
    return todos


def solution(board):
    NY = len(board)
    NX = len(board[0])
    INF = 999
    board_min = [[INF for i in range(NX)] for j in range(NY)]    
    
    # find initial position "R" and goal "G"
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val == "R": 
                Rx = x
                Ry = y
            if val == "G":
                Gx = x
                Gy = y

    todos = [(0, Rx, Ry)]
    
    while todos:
        N_move, x, y = heapq.heappop(todos)
        
        if N_move >= board_min[y][x]: continue
        
        board_min[y][x] = N_move
        todos = find_nexts(N_move + 1, x, y, todos, board, NX, NY)
        
    result = board_min[Gy][Gx]
    return result if result < 999 else -1