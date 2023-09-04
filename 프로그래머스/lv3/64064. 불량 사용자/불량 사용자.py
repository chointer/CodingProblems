from itertools import combinations

def ismatch(user, banned):
    if len(user) != len(banned):
        return False
    for i, s in enumerate(banned):
        if s == '*':
            continue
        if s != user[i]:
            return False
    return True

def DFS(left, visits, graph):
    if not left: 
        return True
    
    for v in graph[left[0]]:
        if not visits[v]:
            visits[v] = True
            if DFS(left[1:], visits, graph):
                return True
            visits[v] = False
    
    return False
    

def solution(user_id, banned_id):
    graph = []
    for banned in banned_id:
        tmp = []
        for i, user in enumerate(user_id):
            if ismatch(user, banned):
                tmp.append(i)
        graph.append(tmp)

    count = 0
    ban_list = [i for i in range(len(banned_id))]
    for com in combinations([i for i in range(len(user_id))], len(banned_id)):
        visits = [True for i in range(len(user_id))]
        for c in com:
            visits[c] = False
        if DFS(ban_list, visits, graph):
            count += 1
    
    return count