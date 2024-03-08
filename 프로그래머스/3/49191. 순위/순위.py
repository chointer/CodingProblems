# n <= 100, matches <= 4500
# 각 선수에 대해 계산해도 시간이 부족하지 않을 것 같다.

def BFS(player, graph, n):
    count = 0
    lis = [player]
    visits = [False for _ in range(n + 1)]
    # visits[player] = True
    
    while lis:
        player = lis.pop()
        for p in graph[player]:
            if not visits[p]:
                count += 1
                visits[p] = True
                lis.append(p)
    
    return count


def solution(n, results):
    wins = {i + 1: [] for i in range(n)}
    loses = {i + 1: [] for i in range(n)}
    for winner, loser in results:
        wins[winner].append(loser)
        loses[loser].append(winner)
    
    answer = 0
    for i in range(1, n + 1):
        if BFS(i, wins, n) + BFS(i, loses, n) == n - 1:
            answer += 1
    return answer