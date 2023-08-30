import heapq

def solution(n, edge):
    # graph
    graph = {i: [] for i in range(1, n + 1)}
    for nd1, nd2 in edge:
        graph[nd1].append(nd2)
        graph[nd2].append(nd1)
    
    # search
    costs = [50000 for i in range(n + 1)]
    tasks = [(0, 1)]    # (cost, node_id)

    while tasks:
        cost, node = heapq.heappop(tasks)
        if cost < costs[node]:
            costs[node] = cost
            for next_node in graph[node]:
                heapq.heappush(tasks, (cost+1, next_node))
    
    # find max costs
    count = 0
    cost_max = max(costs[1:])
    for i, cost in enumerate(costs):
        if cost == cost_max:
            count += 1

    return count