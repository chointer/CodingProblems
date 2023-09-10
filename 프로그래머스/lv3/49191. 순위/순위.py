# 각 선수별로 위로 몇 명, 아래로 몇 명인지 확인하면? 100 * 4500 ~ 1e6 / 2
# 승리와 패배, 각 단방향으로 Floyd-Warshall?
# 틀렸는데, 플로이드 워셜을 구현이 잘못되어서 그랬다. 순서가 중요한지 몰랐다.
# for i, j, k에 대해, "ij edge를 k 경유하는 경우 체크"로 했는데,
# "i를 경유해서 jk를 갈 때를 체크"하는 식으로 해야 한다.

def solution(n, results):
    INF = 1
    graph_win = [[INF for _ in range(n)] for _ in range(n)]
    graph_lose = [[INF for _ in range(n)] for _ in range(n)]
    for w, l in results:
        w -= 1
        l -= 1
        graph_win[w][l] = 0
        graph_lose[l][w] = 0
    for i in range(n):
        graph_win[i][i] = 0
        graph_lose[i][i] = 0
        
    # Floyd-Warshall; D_ij = min(D_ij, D_ik + D_kj)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph_win[j][k] = \
                    min(graph_win[j][k], graph_win[j][i]+graph_win[i][k])
                graph_lose[j][k] = \
                    min(graph_lose[j][k], graph_lose[j][i]+graph_lose[i][k])

    count = 0
    for wins, loses in zip(graph_win, graph_lose):
        is_ranked = True
        for w, l in zip(wins, loses):
            if w * l == 1:
                is_ranked = False
        if is_ranked: count += 1
    
    return count