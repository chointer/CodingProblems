# N <= 1e2
# 단순히 순서대로 체크하면 N**2 <= 1e4  * 10(=rank 개수)
# priorities에서 target을 기록할 자료형으로 바꾼다.
# target이 지워질 때까지 체크한다.

from collections import Counter, deque

def solution(priorities, location):
    counts = Counter(priorities)
    priorities = deque([(p, i) for i, p in enumerate(priorities)])
    dones = 0
    
    while priorities:
        rank, idx = priorities.popleft()

        if rank == max(counts.keys()):
            dones += 1
            counts[rank] -= 1
            if counts[rank] == 0:
                del counts[rank]
            if idx == location:
                return dones     
            
        else:
            priorities.append((rank, idx))
        
    return -1







"""
def solution(priorities, location):
    loc = [False] * len(priorities)
    loc[location] = True
    order = 0
    
    while priorities:
        idx_max = priorities.index(max(priorities))
        
        if idx_max != 0:
            priorities = priorities[idx_max:] + priorities[:idx_max]
            loc = loc[idx_max:] + loc[:idx_max]
        
        if loc[0] == True: break
        
        priorities.pop(0)
        loc.pop(0)
        order += 1
            
    return order + 1
"""