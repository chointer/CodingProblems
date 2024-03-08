# 전위: root - L - R
# 후위: L - R - root
# n <= 1e4
# depth <= 1e3, width <= 1e5
# 트리를 먼저 만들어야할 것 같은데...
# 
import heapq
import sys
sys.setrecursionlimit(10000)

class node():
    def __init__(self, x, y, idx):
        self.name = idx
        self.x = x
        self.y = y
        self.L = None
        self.R = None
        
def allocate(x, y, idx, root):
    if root.x < x:
        if root.R is not None:
            allocate(x, y, idx, root.R)
        else:
            root.R = node(x, y, idx)
        
    else:
        if root.L is not None:
            allocate(x, y, idx, root.L)
        else:
            root.L = node(x, y, idx)
            
def preorder(node, trace):
    trace.append(node.name)
    if node.L:
        trace = preorder(node.L, trace)
    if node.R:
        trace = preorder(node.R, trace)
    return trace

def postorder(node, trace):
    if node.L:
        trace = postorder(node.L, trace)
    if node.R:
        trace = postorder(node.R, trace)
    trace.append(node.name)
    return trace

def solution(nodeinfo):
    hq = []
    for i, info in enumerate(nodeinfo):
        heapq.heappush(hq, (-info[1], info[0], i + 1))

    # Root
    y, x, idx = heapq.heappop(hq)
    root = node(x, y, idx)
    
    # make tree
    while hq:
        y, x, idx = heapq.heappop(hq)
        allocate(x, y, idx, root)
    
    answer = [preorder(root, []), postorder(root, [])] 

    return answer