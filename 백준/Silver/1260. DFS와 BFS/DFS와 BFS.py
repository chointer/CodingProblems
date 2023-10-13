from collections import deque
import sys

def dfs(pos, result, graph, visits):
    for nex in graph[pos]:
        if not visits[nex]:
            visits[nex] = True
            result.append(nex)
            result = dfs(nex, result, graph, visits)
    return result
    

N, M, V = map(int, input().split())

# graph
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for k in graph.keys():
    graph[k].sort()

# DFS
visits = [False for _ in range(N + 1)]
visits[V] = True
DFS = dfs(V, [V], graph, visits)
DFS = list(map(str, DFS))
print(" ".join(DFS))

# BFS
visits = [False for _ in range(N + 1)]
visits[V] = True
q = deque([V])
BFS = [V]

while q:
    v = q.popleft()
    for nex in graph[v]:
        if not visits[nex]:
            visits[nex] = True
            BFS.append(nex)
            q.append(nex)
BFS = list(map(str, BFS))
print(" ".join(BFS))
