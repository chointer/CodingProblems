# union-find도 될 것 같은데, BFS로 풀어보기
# O(N**2) -> 40000

from collections import deque

def dfs(start, visits, computers):
    q = deque([start])
    
    while q:
        now = q.popleft()
        
        if visits[now]:
            continue
        
        visits[now] = True

        for i, connect in enumerate(computers[now]):
            if connect == 1 and not visits[i]:
                q.append(i)
    
    return visits



def solution(n, computers):
    N_networks = 0
    visits = [False for i in range(n)]

    for i in range(n):
        if visits[i]:
            continue
        
        else:
            N_networks += 1
            visits = dfs(i, visits, computers)

    return N_networks