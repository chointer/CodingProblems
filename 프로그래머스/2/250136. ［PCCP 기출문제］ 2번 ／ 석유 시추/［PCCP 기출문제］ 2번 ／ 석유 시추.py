# 500 * 500
# 완전탐색? and range?

import heapq
def search_area(x, y, land):
    ysize = len(land)
    xsize = len(land[0])
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    
    xmin, xmax = x, x
    stack = [(y, x)]
    area = 0
    
    while stack:
        y, x = stack.pop()
        if land[y][x] == 0:
            continue
        else:
            land[y][x] = 0
            area += 1
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            
            for dx, dy in zip(dxs, dys):
                x_temp = x + dx
                y_temp = y + dy
                if x_temp >= 0 and x_temp < xsize and \
                y_temp >= 0 and y_temp < ysize and \
                land[y_temp][x_temp] == 1:
                    stack.append((y_temp, x_temp))
    
    return (xmin, xmax, area)
    

def search_oils(land):
    oils = []
    for y, la in enumerate(land):
        for x, l in enumerate(la):
            if l == 1:
                oils.append(search_area(x, y, land))
    return oils
    
def solution(land):
    oils = search_oils(land)

    hq = []
    for oil in oils:
        heapq.heappush(hq, (oil[0], oil[2]))
        heapq.heappush(hq, (oil[1] + 1, -oil[2]))
    
    max_amount = 0
    amount = 0
    while hq:
        x, area = heapq.heappop(hq)
        amount += area
        max_amount = max(max_amount, amount)
    
    return max_amount