# 17m 58s
def solution(m, n, puddles):
    maps = [[0 for _ in range(m)] for _ in range(n)]  # Num of ways
    maps[0][0] = 1
    pud = []
    for p in puddles:
        pud.append([p[0]-1, p[1]-1])
        
    for i in range(1, m + n - 1):
        for j in range(i + 1):
            x = j
            y = i - j
            if x >= 0 and y >= 0 and x < m and y < n and [x, y] not in pud:
                if y == 0:
                    maps[y][x] = maps[y][x-1]
                elif x == 0:
                    maps[y][x] = maps[y-1][x]
                else:
                    maps[y][x] = (maps[y][x-1] + maps[y-1][x])%1000000007
    return maps[-1][-1]