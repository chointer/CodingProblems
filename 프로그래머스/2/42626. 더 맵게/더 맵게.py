# N <= 1e6
# heapq로 가장 작은 음식 두 개 pop

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    
    count_mix = 0
    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        count_mix += 1
    
    
    return count_mix if scoville[0] >= K else -1