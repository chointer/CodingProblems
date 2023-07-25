# Four edges for each node.
# union-find algorithm: for an node, find next node, and union.
# nodes: (x, y, d)
# d is the absolute direction. 0,1,2,3: up, right, down, left
# S: d -> d
# L: d -> (d-1)%4
# R: d -> (d+1)%4

from collections import defaultdict

def next_edge(x, y, d, grid, X, Y):
    if d == 0:
        next_x, next_y = x, (y+1)%Y
    elif d == 1:
        next_x, next_y = (x+1)%X, y
    elif d == 2:
        next_x, next_y = x, (y-1)%Y
    elif d == 3:
        next_x, next_y = (x-1)%X, y
    else:
        assert False, (x, y, d)
    
    node = grid[next_y][next_x]
    if node == 'S':
        next_d = d
    elif node == 'R':
        next_d = (d+1)%4
    elif node == 'L':
        next_d = (d-1)%4
    else:
        assert False, (x, y, d, node)
        
    return next_x, next_y, next_d
    
    
def find(edgedict, edge):
    if edgedict[edge] != edge:
        edgedict[edge] = find(edgedict, edgedict[edge])
    return edgedict[edge]
        
    
def union(edgedict, edge, next_edge):
    ori_edge = find(edgedict, edge)
    
    if next_edge not in edgedict:
        edgedict[next_edge] = ori_edge
        return

    ori_next_edge = find(edgedict, next_edge)
    
    if ori_edge < ori_next_edge:
        edgedict[ori_next_edge] = ori_edge
    else:
        edgedict[ori_edge] = ori_next_edge

    return #edgedict
    
    
def solution(grid):
    X = len(grid[0]); Y = len(grid)
    edge2edge = {}      # key: edge,  node: origin_edge
    
    for y in range(Y):
        for x in range(X):
            for d in range(4):
                if (x, y, d) not in edge2edge:
                    edge2edge[(x, y, d)] = (x, y, d)
                # (x, y, d)
                next_x, next_y, next_d = next_edge(x, y, d, grid, X, Y)
                union(edge2edge, (x, y, d), (next_x, next_y, next_d))
    
    # final update
    for y in range(Y):
        for x in range(X):
            for d in range(4):
                find(edge2edge, (x, y, d))

    # counting
    count = defaultdict(int)
    for y in range(Y):
        for x in range(X):
            for d in range(4):
                count[edge2edge[(x, y, d)]] += 1
    
    answer = list(count.values())
    answer.sort()
    
    return answer