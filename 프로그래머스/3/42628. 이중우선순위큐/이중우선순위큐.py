# O(N) = NlogN*4

import heapq as hq
from collections import defaultdict

def solution(operations):
    maxq = []
    minq = []
    max_delays = defaultdict(int)
    min_delays = defaultdict(int)
    
    for operation in operations:
        oper, val = operation.split()
        if oper == "I":
            hq.heappush(maxq, -int(val))
            hq.heappush(minq, int(val))
            
        elif val == "1":
            while maxq and max_delays[-maxq[0]] > 0:
                del_val = -hq.heappop(maxq)
                max_delays[del_val] -= 1
            if maxq:
                max_val = -hq.heappop(maxq)
                min_delays[max_val] += 1
                
        elif val == "-1":
            while minq and min_delays[minq[0]] > 0:
                del_val = hq.heappop(minq)
                min_delays[del_val] -= 1
            if minq:
                min_val = hq.heappop(minq)
                max_delays[min_val] += 1

    ### END
    while maxq and max_delays[-maxq[0]] > 0:
        del_val = -hq.heappop(maxq)
        max_delays[del_val] -= 1
    if maxq:
        max_val = -hq.heappop(maxq)
    else:
        max_val = 0

    while minq and min_delays[minq[0]] > 0:
        del_val = hq.heappop(minq)
        min_delays[del_val] -= 1
    if minq:
        min_val = hq.heappop(minq)
    else:
        min_val = 0

    return [max_val, min_val]

    
"""
def solution(operations):
    q = []
    
    for oper in operations:
        op1, op2 = oper.split()
        if op1 == 'I':
            q.append(int(op2))
            q.sort()
            
        elif op1 == 'D' and q:
            if op2 == '1':
                del q[-1]
            elif op2 == '-1':
                del q[0]
                
    
    if q:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]
    return answer
"""