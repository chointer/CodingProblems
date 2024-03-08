# N <= 100. costs < 5000
# parent가 다르면 union & 건설
# parent가 같으면 pass

def find(x, parents):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(a, b, parents):
    pa = find(a, parents)
    pb = find(b, parents)
    if pa < pb:
        parents[pb] = pa
        return True
    elif pa > pb:
        parents[pa] = pb
        return True
    else:
        return False
        
        
def solution(n, costs):
    parents = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])
    answer = 0
    
    for a, b, cost in costs:
        unioned = union(a, b, parents)
        if unioned:
            answer += cost
    
    for i in range(n):
        parents[i] = find(i, parents)
        
    return answer