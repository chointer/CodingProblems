# N <= 1e2
# 완성 날 기록. 첫 작업의 완성 날보다 작은 것들 popleft.
# O(N) = N

import math
from collections import deque

def solution(progresses, speeds):
    enddates = deque([math.ceil((100 - progress)/speed) for progress, speed in zip(progresses, speeds)])
    print(enddates)
    
    answer = []
    count = 1
    end_date = enddates.popleft()
    ref_date = end_date
    
    while enddates:
        end_date = enddates.popleft()
        
        if end_date <= ref_date:
            count += 1
        else:
            answer.append(count)
            count = 1
            ref_date = end_date
    
    answer.append(count)
    
    return answer
    












"""
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        # add
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # distribute
        count = 0
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
            if not progresses: break
        if count != 0:
            answer.append(count)
    
    return answer
"""