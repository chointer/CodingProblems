# 53m
# Edges <= 1e6, Graphs >= 2
# 생성 정점은 도착 node가 없고, 시작 node가 2개 이상.
# 생성 정점을 먼저 찾아야 한다. O(1e6)
# 1) table 생성; 단방향 table & 양방향 table
# 2) 생성 정점 찾고, visits 체크
# 3) 완전 탐색으로 그래프를 찾고 제거한다.

# 다른 솔루션을 봤는데, 완전 탐색을 할 필요가 없었다.
# 도넛을 제외한 생성 정점과 막대, 8자 그래프는 고유한 하나의 노드가 존재한다.
# 노드를 탐색하면서 해당 특징을 가진 노드를 발견하면 count.
# 생성 정점에서 나가는 간선 개수로 총 그래프 수를 구해서, 도넛 그래프의 개수를 구한다.

from collections import defaultdict

def solution(edges):
    answer = []
    
    # Node Tables
    oneWays = defaultdict(list)
    twoWays = defaultdict(list)
    N = 0
    for a, b in edges:
        N = max([N, a, b])
        oneWays[a].append(b)
        twoWays[a].append(b)
        twoWays[b].append(a)
        
    # Find Core Node
    for i in range(1, N + 1):
        if (len(oneWays[i]) == len(twoWays[i])) and (len(oneWays[i]) >= 2):
            answer.append(i)
            visits = [False for _ in range(N + 1)]
            visits[i] = True
            break
    
    # Find Graphs using TwoWay Table
    graphs = []
    for n in range(1, N + 1):
        if visits[n]:
            continue
        
        N_GraphNodes = 0
        N_GraphEdges = 0
        stack = [n]
        
        while stack:
            node = stack.pop()
            if visits[node]: continue
            
            N_GraphEdges += len(oneWays[node])
            N_GraphNodes += 1
            visits[node] = True
            
            for e in twoWays[node]:
                if not visits[e]:
                    stack.append(e)
        graphs.append((N_GraphNodes, N_GraphEdges))
    
    # Classify graphs
    N_Stick = 0
    N_Donut = 0
    N_Eight = 0
    for n_nodes, n_edges in graphs:
        gap = n_nodes - n_edges
        if gap == 0:
            N_Donut += 1
        elif gap == 1:
            N_Stick += 1
        elif gap == -1:
            N_Eight += 1
        else:
            print(n_nodes, n_edges)
    
    answer += [N_Donut, N_Stick, N_Eight]
    return answer
