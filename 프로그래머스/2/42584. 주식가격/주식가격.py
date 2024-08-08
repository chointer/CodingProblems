# N <= 1e5
# price 내림차순으로 기록(heapq?)하고, t시점에서, price보다 높은 과거 기록은 모두 갱신
# 마지막에 나머지들 후처리?

import heapq
def solution(prices):
    answers = [-1 for i in range(len(prices))]
    hq = []
    
    for t, p in enumerate(prices):
        while hq and -hq[0][0] > p:
            pp, tt = heapq.heappop(hq)
            answers[tt] = t - tt
        
        heapq.heappush(hq, (-p, t))
    
    T = len(prices) - 1
    for i, val in enumerate(answers):
        if val == -1:
            answers[i] = T - i
    
    return answers