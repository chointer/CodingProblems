from collections import deque

def solution(sequence):
    sequence1 = deque(sequence)
    seq_sum = [sequence1.popleft()]
    sign = -1
    while sequence1:
        seq_sum.append(seq_sum[-1] + sign*sequence1.popleft())
        sign *= -1
    
    sum_min = min(seq_sum)
    sum_max = max(seq_sum)
    answer = max([sum_max, -sum_min, sum_max - sum_min])
    
    return answer