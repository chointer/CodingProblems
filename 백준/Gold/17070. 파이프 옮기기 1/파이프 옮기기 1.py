N = int(input())
maps = []
for n in range(N):
    maps.append(list(map(int, input().split())))

# Index. 0: horizontal, 1: vertial, 2: diagonal
maps_count = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
maps_count[0][1][0] = 1

for xy in range(2 * N - 1):
    for x in range(xy + 1):
        y = xy - x
        if y >= N or x >= N or maps[y][x] == 1: 
            continue
        
        # [0] Horizontal
        if x >= 1:
            maps_count[y][x][0] += maps_count[y][x - 1][0] + maps_count[y][x - 1][2]
        
        # [1] Vertial
        if y >= 1:
            maps_count[y][x][1] += maps_count[y - 1][x][1] + maps_count[y - 1][x][2]
            
        # [2] Diagonal
        if x >= 1 and maps[y][x - 1] == 0 and y >= 1 and maps[y - 1][x] == 0:
            maps_count[y][x][2] += sum(maps_count[y - 1][x - 1])
            
print(sum(maps_count[N - 1][N - 1]))