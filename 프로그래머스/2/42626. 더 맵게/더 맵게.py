# N <= 1e6, K <= 1e9, el <= 1e6
# 두 음식을 섞으면, 총 음식 수가 1개 감소한다. -> 최대 반복 가능 횟수 = 1e6

import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    
    count_mix = 0
    while len(scoville) > 1 and scoville[0] < K:
        min0 = hq.heappop(scoville)
        min1 = hq.heappop(scoville)
        hq.heappush(scoville, min0 + 2 * min1)
        count_mix += 1
    
    if scoville and scoville[0] < K:
        return -1
    else:
        return count_mix

"""
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
            
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        answer += 1
        
    return answer
"""