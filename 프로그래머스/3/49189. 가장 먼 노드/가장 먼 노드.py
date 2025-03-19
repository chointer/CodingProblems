# N <= 2e4, E <= 5e4
# 각 노드별 거리를 구하고 카운트 해야 한다.
# O(N) = E + N log N? 알아보기

import heapq as hq

def solution(n, edge):
    # edge list
    edge_list = [[] for _ in range(n)]
    for p1, p2 in edge:
        p1 -= 1
        p2 -= 1
        edge_list[p1].append(p2)
        edge_list[p2].append(p1)

    # search
    distances = [n + 1 for _ in range(n)]
    distances[0] = 0
    checks = [(0, 0)]        # (distance, node_id - 1)
    
    while checks:
        dist, node = hq.heappop(checks)
        if distances[node] < dist:
            continue
                
        for neighbor in edge_list[node]:
            if distances[neighbor] > dist + 1:
                distances[neighbor] = dist + 1
                hq.heappush(checks, (dist + 1, neighbor))
        
    distance_farthest = 0
    count = 1
    for i in distances:
        if distance_farthest < i:
            distance_farthest = i
            count = 1
        elif distance_farthest == i:
            count += 1
    
    return count