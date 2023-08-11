import heapq
from collections import deque

def solution(k, score):
    score = deque(score)
    rank = []
    answer = []
    
    for d in range(min(k, len(score))):        # not fully filled rank
        heapq.heappush(rank, score.popleft())
        answer.append(rank[0])
    
    while score:
        sc = score.popleft()
        if sc > rank[0]:
            heapq.heappop(rank)
            heapq.heappush(rank, sc)
        answer.append(rank[0])
    
    return answer