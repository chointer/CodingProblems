# N <= 1e5, 값 범위 <= 1e4
# 처리 우선 순위를 heapq로 관리한다. k-th val보다 큰 것들은 k 시점에 모두 처리한다.
# O(N) = NlogN

import heapq

def solution(prices):
    answers = [-1 for _ in range(len(prices))]
    hqs = []
    
    for i, price in enumerate(prices):
        heapq.heappush(hqs, (-price, i))
        
        while hqs and -hqs[0][0] > price:
            _, idx = heapq.heappop(hqs)
            answers[idx] = i - idx
    
    while hqs:
        _, idx = heapq.heappop(hqs)
        answers[idx] = i - idx
    
    return answers
    
    
    
    
    

    
"""
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
"""