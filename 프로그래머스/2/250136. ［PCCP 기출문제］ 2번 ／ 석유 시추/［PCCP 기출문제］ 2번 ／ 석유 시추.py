# land <= (500, 500)

import heapq

def dfs(y, x, land, W, H):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = [(y, x)]
    amount = 0
    x0 = x
    x1 = x
    
    while stack:
        y, x = stack.pop()
        if land[y][x] == 0:
            continue
        else:
            land[y][x] = 0
            amount += 1
            x0 = min(x0, x)
            x1 = max(x1, x)
            
        for dy, dx in moves:
            yy = y + dy
            xx = x + dx
            if yy >= 0 and yy < H and xx >= 0 and xx < W and land[yy][xx] == 1:
                stack.append((yy, xx))
    return x0, x1, amount
    
def solution(land):
    H = len(land)
    W = len(land[0])
    deposits = []       # (x0, x1, amount)
    
    for y in range(H):
        for x in range(W):
            if land[y][x] == 1:
                deposits.append(dfs(y, x, land, W, H))
    
    hq = []
    for deposit in deposits:
        x0, x1, a = deposit
        heapq.heappush(hq, (x0, a))
        heapq.heappush(hq, (x1 + 1, -a))
    
    amount_max = 0
    amount_current = 0
    
    for x in range(W):
        while hq[0][0] <= x:
            _, a = heapq.heappop(hq)
            amount_current += a
        amount_max = max(amount_max, amount_current)
        
    return amount_max