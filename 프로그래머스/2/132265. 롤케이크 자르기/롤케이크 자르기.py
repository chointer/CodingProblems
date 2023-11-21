# topping <= 1e6
# 6m 14s
# 이진탐색도 된다.

from collections import Counter

def solution(topping):
    me = Counter()
    bro = Counter(topping)
    n_me = 0
    n_bro = len(bro.keys())
    
    answer = 0
    for topp in topping:
        me[topp] += 1
        if me[topp] == 1:
            n_me += 1
        
        bro[topp] -= 1
        if bro[topp] == 0:
            n_bro -= 1
            
        if n_me == n_bro:
            answer += 1
        elif n_me > n_bro:
            break
    
    return answer