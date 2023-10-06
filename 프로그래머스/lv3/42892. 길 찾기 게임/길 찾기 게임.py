# 일부 테스트 케이스를 실패했는데 원인을 찾지 못해서 (시간도 오래 지난김에) 새로 구현
# N of Nodes <= 1e4, Depth <= 1e3
import sys
sys.setrecursionlimit(1200)

class node():
    def __init__(self, x, y, n):
        self.r = None
        self.l = None
        self.x = x
        self.y = y
        self.n = n
        
def pre_search(parent, nodes, ans=[]):   # root L R
    ans.append(parent.n + 1)
    if parent.l is not None:
        ans = pre_search(nodes[parent.l], nodes, ans)
    if parent.r is not None:
        ans = pre_search(nodes[parent.r], nodes, ans)
    return ans
    
def post_search(parent, nodes, ans=[]):  # L R root
    if parent.l is not None:
        ans = post_search(nodes[parent.l], nodes, ans)
    if parent.r is not None:
        ans = post_search(nodes[parent.r], nodes, ans)
    ans.append(parent.n + 1)
    return ans
    
def solution(nodeinfo):
    nodes = [node(x, y, n) for n, (x, y) in enumerate(nodeinfo)]
    nodes_sort = sorted(nodes, key=lambda no: [-no.y, no.x])
    root_idx = nodes_sort.pop(0).n
    
    for no in nodes_sort:
        parent = nodes[root_idx]
        while True:
            if no.x < parent.x:
                if parent.l is not None:
                    parent = nodes[parent.l]
                else:
                    parent.l = no.n
                    break
                    
            else: ## no.x > parent.x
                if parent.r is not None:
                    parent = nodes[parent.r]
                else:
                    parent.r = no.n
                    break
    
    answer = []
    answer.append(pre_search(nodes[root_idx], nodes))
    answer.append(post_search(nodes[root_idx], nodes))
    
    return answer