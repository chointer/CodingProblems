# 각 칸마다 4개의 방향 존재. 각 칸마다, 각 방향으로 가는 길은 한 번 사용되면 다른 사이클에서는 더 이상 사용되지 않는다.
# {(h, w): {'up': -1, 'low': -1, 'left': -1, 'right': -1}}
# O(N) = 500*500

# DIRECTIONS: 0: 'up', 1: 'right', 2: 'low', 3: 'left'

def find_cycle(st_y, st_x, st_di, grid, grid_h, grid_w, cycle_id, cycle_map):
    moves = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    
    count = 0
    current_y = st_y
    current_x = st_x
    current_di = st_di
    
    while cycle_map[(current_y, current_x)][current_di] < 0:
        cycle_map[(current_y, current_x)][current_di] = cycle_id
        count += 1
        
        # next point
        current_y = (current_y + moves[current_di][0]) % grid_h
        current_x = (current_x + moves[current_di][1]) % grid_w
        
        # next dir
        if grid[current_y][current_x] == 'L':
            current_di = (current_di - 1)%4
        elif grid[current_y][current_x] == 'R':
            current_di = (current_di + 1)%4
        else:   # 'S'
            current_di = current_di
    
    return count
    
    
def solution(grid):
    H = len(grid)
    W = len(grid[0])
    
    # make dictionary
    cycle_map = {}
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            cycle_map[(y, x)] = {i: -1 for i in range(4)}       # directions
    
    # 순회
    cycle_id = 0
    cycle_counts = []       # 각 id마다 경로의 길이
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            for direction_start in range(4):
                if cycle_map[(y, x)][direction_start] < 0:
                    count = find_cycle(y, x, direction_start, grid, H, W, cycle_id, cycle_map)
                    cycle_counts.append(count)
                    cycle_id += 1
    
    return sorted(cycle_counts)