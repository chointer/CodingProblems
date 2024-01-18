# length <= 1e6, val <= 1e5
# 주제가 stack & queue. => 흠. 모르겠다. 
# 순서대로 체크(stack)하고 트리거가 되면 일괄 처리(pop) 같은데
# heapq?
import heapq

def solution(prices):
    length = len(prices)
    hq = []
    answer = [-1 for _ in range(length)]
    
    for t, price in enumerate(prices):
        heapq.heappush(hq, (-price, t))
        while hq and hq[0][0] < -price:
            _, idx = heapq.heappop(hq)
            answer[idx] = t - idx
    
    
    for i, val in enumerate(answer):
        if val == -1:
            answer[i] = length - i - 1
    return answer