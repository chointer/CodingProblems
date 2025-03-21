# priorities <= 1e2
# 그냥 구현?
from collections import deque, Counter

def solution(priorities, location):
    # sort map: [[priority, n], ...]
    counter = Counter(priorities)
    sort_map = []
    for p, n in counter.items():
        sort_map.append([p, n])
    sort_map.sort(reverse=True)
    sort_map = deque(sort_map)
    
    priorities = deque([(p, i) for i, p in enumerate(priorities)])
    goal_process = (priorities[location])
    
    # process managing
    order = 1
    while priorities:
        pop = priorities.popleft()
        if pop[0] < sort_map[0][0]:
            priorities.append(pop)
        elif pop[0] == sort_map[0][0]:
            sort_map[0][1] -= 1
            if pop == goal_process:
                return order
            if sort_map[0][1] == 0:
                sort_map.popleft()
            order += 1
    return -1