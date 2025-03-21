# N <= 1e2
# N^3 까지도 가능
# 간선마다, 모두 체크? UnionFind. N * N * N     (for each node * check all * parents finding)

from collections import defaultdict

def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(a, b, parents):
    pa = find(a, parents)
    pb = find(b, parents)
    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb
    return parents

        
def solution(n, wires):    
    min_diff = n
    
    # for each cut,
    for idx_skip in range(len(wires)):
        # union-find
        parents = [i for i in range(n + 1)]
        for i, wire in enumerate(wires):
            if i == idx_skip: continue
            union(wire[0], wire[1], parents)
        
        # count
        counts = defaultdict(int)
        for i in range(1, n + 1):
            counts[find(i, parents)] += 1
        counts = [num for num in counts.values()]
        min_diff = min(min_diff, abs(counts[0]-counts[1]))
        
    return min_diff