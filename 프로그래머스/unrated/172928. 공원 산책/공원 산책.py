def solution(park, routes):
    directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    width = len(park[0])
    height = len(park)
    
    # initial position
    for j, pa in enumerate(park):
        for i, p in enumerate(pa):
            if p == 'S':
                x = i
                y = j
    
    # steps
    for route in routes:
        op, n = route.split()
        dy, dx = directions[op]
        x_temp = x
        y_temp = y

        for i in range(int(n)):
            x_temp += dx
            y_temp += dy
            if x_temp < 0 or x_temp >= width or y_temp < 0 or y_temp >= height or park[y_temp][x_temp] == 'X':
                break
        else:
            x = x_temp
            y = y_temp
        
    return [y, x]