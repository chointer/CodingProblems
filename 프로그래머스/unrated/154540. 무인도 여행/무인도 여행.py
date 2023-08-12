# 처음 코드로 아래 case를 해결하지 못했음. 
# root가 되는 좌표 기준이 명확하지 못했기 때문. (union을 제대로 구현하지 않아서)
# "XXX1X"
# "X1234"
# "X3XXX"

from collections import defaultdict

def find(loc, maps_root):
    root = maps_root[loc[0]][loc[1]]
    if root == loc:
        return root
    else:
        return find(root, maps_root)        

def union(a, b, maps_root):
    pa = find(a, maps_root)
    pb = find(b, maps_root)
    if pa >= pb:
        maps_root[pa[0]][pa[1]] = pb
    else:
        maps_root[pb[0]][pb[1]] = pa
        

def solution(maps):
    X, Y = len(maps[0]), len(maps)
    maps_root = [[(i, j) for j in range(X)] for i in range(Y)]
    
    for y in range(Y):
        for x in range(X):
            # ocean check
            if maps[y][x] == 'X':
                continue

            loc = (y, x)
            
            # search (left & down)
            if x + 1 < X and maps[y][x+1] != 'X':
                union(loc, (y, x+1), maps_root)
            if y + 1 < Y and maps[y+1][x] != 'X':
                union(loc, (y+1, x), maps_root)
    
    island_dict = defaultdict(int)
        
    for y in range(Y):
        for x in range(X):
            if maps[y][x] != 'X':
                loc = (y, x)
                root = find(loc, maps_root)
                island_dict[root] += int(maps[y][x])

    return sorted(island_dict.values()) if island_dict else [-1]