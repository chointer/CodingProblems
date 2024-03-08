# '1'에서 각 노드까지의 거리 계산

import heapq
def solution(n, edge):
    node_dict = {i: [] for i in range(1, n + 1)}
    for e in edge:
        node_dict[e[0]].append(e[1])
        node_dict[e[1]].append(e[0])
    
    dists = [100000 for i in range(n + 1)]
    dists[1] = 0
    hq = [(0, 1)]           # dist, node
    
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > dists[node]:
            continue
        
        for to in node_dict[node]:
            if dist + 1 < dists[to]:
                dists[to] = dist + 1
                heapq.heappush(hq, (dist + 1, to))
        
    dist_max = max(dists[1:])
    
    return dists.count(dist_max)