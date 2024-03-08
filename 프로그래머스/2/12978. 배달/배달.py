# Floyd-Warshall 연습.

def solution(N, road, K):
    inf = 100000000
    roads = [[inf for _ in range(N)] for _ in range(N)]
    for i in range(N):
        roads[i][i] = 0
        
    for a, b, c in road:
        if roads[a - 1][b - 1] > c:
            roads[a - 1][b - 1] = c
            roads[b - 1][a - 1] = c
        
    # Floyd-Warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if roads[i][j] > roads[i][k] + roads[k][j]:
                    roads[i][j] = roads[i][k] + roads[k][j]

    count = 0
    for c in roads[0]:
        if c <= K:
            count += 1
    return count