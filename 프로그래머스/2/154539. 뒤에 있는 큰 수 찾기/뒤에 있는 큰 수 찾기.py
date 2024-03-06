# L, N <= 1e6
# heapq로 스택?

import heapq
def solution(numbers):
    q = []      # (n, idx)
    answer = [-1 for i in range(len(numbers))]
    
    for i, num in enumerate(numbers):
        heapq.heappush(q, (num, i))
        
        while q and q[0][0] < num:
            _, recorded_idx = heapq.heappop(q)
            answer[recorded_idx] = num
        
    return answer