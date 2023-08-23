# Dijkstra?
import heapq

def solution(n, roads, sources, destination):
    # roadmap from roads
    roadmap = [[] for _ in range(n + 1)]
    for a, b in roads:
        roadmap[a].append(b)
        roadmap[b].append(a)
    
    # Dijkstra from destination
    INF = int(1e7)
    times = [INF for _ in range(n+1)]
    tasks = [(0, destination)]           # (time, loc)
    
    while tasks:
        time, loc = heapq.heappop(tasks)
        if time >= times[loc]:
            continue
        else:
            times[loc] = time
            for loc_next in roadmap[loc]:
                heapq.heappush(tasks, (time + 1, loc_next))
    
    # results
    answer = []
    for source in sources:
        t = times[source]
        if t == INF:
            answer.append(-1)
        else:
            answer.append(t)

    return answer