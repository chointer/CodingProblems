# N <= 50, roads <= 2000
# Dijkstra O( (V+E) log V ) < 1e4?

import heapq
def solution(N, road, K):
    roads = [[] for i in range(N)]
    
    for (a, b, cost) in road:
        a -= 1
        b -= 1
        
        for idx, ra in enumerate(roads[a]):
            if ra[0] == b:
                if ra[1] > cost:
                    roads[a][idx][1] = cost
                break
        else:
            roads[a].append([b, cost])
            
        for idx, rb in enumerate(roads[b]):
            if rb[0] == a:
                if rb[1] > cost:
                    roads[b][idx][1] = cost
                break
        else:
            roads[b].append([a, cost])

    
    INF = 100000000
    costs = [INF for i in range(N)]
    hq = [[0, 0]]
    costs[0] = 0
    
    while hq:
        print(hq)
        cost, loc = heapq.heappop(hq)
        if costs[loc] < cost:
            continue
        for des in roads[loc]:
            new_cost = cost + des[1]
            if costs[des[0]] > new_cost:
                costs[des[0]] = new_cost
                heapq.heappush(hq, [new_cost, des[0]])
    
    return len([c for c in costs if c <= K])