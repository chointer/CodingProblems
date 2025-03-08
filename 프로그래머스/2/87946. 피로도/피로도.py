# k < 5000, N(dungeons) <= 8
# 완탐시, 8P8=8! ~ 40,000

from itertools import permutations

def run_dungeons(k, seq):
    count = 0
    for i, s in enumerate(seq):
        k_in, k_use = s
        if k < k_in:
            break
        else:
            k -= k_use
            count += 1
    return count
            
        
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons):
        answer = max(answer, run_dungeons(k, p))
    return answer