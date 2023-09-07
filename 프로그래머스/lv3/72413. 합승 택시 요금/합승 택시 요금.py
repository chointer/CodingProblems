# N <= 200 -> max ~ N**3?
# (1) S에서 각자 가는 경우 계산: Dijkstra N**2, 모든 위치를 S로 해서 계산? -> N**3
# (2) Floyd-Warshall?  [선택]
# 풀이 중에, s, a, b에 대해 Dijkstra 계산하고, 각 node를 분기점으로 했을 때의 cost를 계산하는 방법이 있었다.

def solution(n, s, a, b, fares):
    # initialize
    s -= 1; a -= 1; b -= 1
    INF = 100000000
    graph = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for i, j, cost in fares:
        graph[i-1][j-1] = cost
        graph[j-1][i-1] = cost
    
    # Floyd-Warshall; D_ij = min(D_ij, D_ik+D_kj)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    # Find
    cost_min = INF
    for i in range(n):
        cost_min = min(cost_min, graph[s][i] + graph[i][a] + graph[i][b])
    
    return cost_min
