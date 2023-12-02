# 모든 node에 대한 최단 경로? -> Dijkstra
# O((V+E) log V) = (1e5 + 5e5)*5 ~= 3e6?

import heapq
def solution(n, roads, sources, destination):
    # 2d graph
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    INF = 1000000
    costs = [INF for _ in range(n + 1)]
    costs[destination] = 0
    hq = [(destination, 0)]         # (목적지, 비용)
    
    while hq:
        des, cost = heapq.heappop(hq)
        if costs[des] < cost: continue
        
        for r in graph[des]:
            if costs[r] > cost + 1:
                costs[r] = cost + 1
                heapq.heappush(hq, (r, cost + 1))

    answer = []
    for s in sources:
        answer.append(costs[s] if costs[s] < INF else -1)
    return answer