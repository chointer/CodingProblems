# edges <= 1e6
# 생성 node는 바깥방향 edge가 3개. (나머지는 최대 2개)
# 1. graph 만들기. O(N) = 1e6
# 2. main node 찾기. O(N) = 1e6
#    (main node는 본인 방향 edge 0개, 외부 방향 edge 2개 이상)
# 3. 각 그래프 탐색: O(N) = 1e6

from collections import defaultdict

def solution(edges):
    # 1. make graph
    graph = defaultdict(list)
    visited = defaultdict(lambda: False)
    graph_num_inverse = defaultdict(int)
    
    for a, b in edges:
        graph[a].append(b)
        graph_num_inverse[b] += 1
        
    # 2. find main node
    for k, v in graph.items():
        if len(v) >= 2 and graph_num_inverse[k] == 0:
            # k: main edge, v: graph start nodes
            visited[k] = True
            break
    
    # 3. graph search
    answer = [k, 0, 0, 0]

    for node in v:
        N_node = 0
        N_edge = 0
        stack = [node]
        while stack:
            n = stack.pop()
            
            if visited[n] is True:
                continue
            else:
                 visited[n] = True
                    
            N_node += 1
            N_edge += len(graph[n])
            
            for n_next in graph[n]:
                stack.append(n_next)

        if N_node == N_edge:
            answer[1] += 1
        elif N_node > N_edge:
            answer[2] += 1
        else:
            answer[3] += 1
            
    return answer