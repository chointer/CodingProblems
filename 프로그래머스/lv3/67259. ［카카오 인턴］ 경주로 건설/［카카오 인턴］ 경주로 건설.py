# board 25*25 = 625
# ( cost, (y1, x1, y2, x2) )
import heapq
from collections import defaultdict

def solution(board):
    # init
    INF = 10000000
    di_ys = [0, 0, 1, -1]
    di_xs = [1, -1, 0, 0]
    boardX = len(board[0])
    boardY = len(board)
    board_cost = defaultdict(lambda: INF)
    steps = []      # ( cost, y0, x0, y1, x1)
    if board[0][1] == 0:
        heapq.heappush( steps, [100, 0, 0, 0, 1] )
    if board[1][0] == 0:
        heapq.heappush( steps, [100, 0, 0, 1, 0] )     
    
    # search
    while steps:
        cost, y0, x0, y1, x1 = heapq.heappop(steps)
        road = (y0, x0, y1, x1) if ((y0 < y1) or (x0 < x1)) else (y1, x1, y0, x0)
        
        if board_cost[road] <= cost:
            continue
            
        board_cost[road] = cost
        direction_pre = (y1 - y0, x1 - x0)     # pre dy, pre dx
        
        for di_y, di_x in zip(di_ys, di_xs):
            px_next = x1 + di_x
            py_next = y1 + di_y
            
            if px_next < 0 or px_next >= boardX or\
            py_next < 0 or py_next >= boardY or\
            board[py_next][px_next] == 1:
                continue
            
            elif di_y == direction_pre[0] and di_x == direction_pre[1]:
                heapq.heappush(steps, [cost + 100, y1, x1, py_next, px_next] )
                
            elif di_y*direction_pre[0] == -1 or di_x*direction_pre[1] == -1:
                continue
            
            else:
                heapq.heappush(steps, [cost + 600, y1, x1, py_next, px_next] )
    
    
    answer = min(board_cost[(boardY-2, boardX-1, boardY-1, boardX-1)],
                 board_cost[(boardY-1, boardX-2, boardY-1, boardX-1)])
    return answer