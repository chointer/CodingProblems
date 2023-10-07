# 앞으로 갈 노드를 기록하고, 그 노드들로 탐색을 각각 해본다. (재귀)
# 2**17 = ~1e5
# 시간복잡도를 어떻게 계산하지?

def search(location, sheep, wolves, candidates, info, tree):
    if info[location] == 0:
        sheep += 1 
    else: 
        wolves += 1
    
    if sheep <= wolves:
        return sheep
    
    candidates = tree[location] | candidates
    if not candidates:
        print("END:", sheep, wolves)
        return sheep
        
    sheep_max = sheep
    for next_step in list(candidates):
        s = search(next_step, sheep, wolves, candidates - set({next_step}), info, tree)
        sheep_max = max(sheep_max, s)

    return sheep_max


def solution(info, edges):
    tree = {i:[] for i in range(len(info))}
    for parent, child in edges:
        tree[parent].append(child)
    for i in range(len(info)):
        tree[i] = set(tree[i])
    
    return search(0, 0, 0, set(), info, tree)