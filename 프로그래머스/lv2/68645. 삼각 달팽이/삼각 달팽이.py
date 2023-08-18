# tri size: (n+1)n/2 < 10**6
# O(N) < build (10**6) + sort (10**6 * log(10**6)) ~ 10**7 ?
# triangular coordinate?

def solution(n):
    pa, pb, pc = -1, n, n-1
    val = 0
    answers = []
    
    # build
    directions = {0: (1, -1, 0), 1: (0, 1, -1), 2: (-1, 0, 1)}
    directionkey = 0
    while n > 0:
        dpa, dpb, dpc = directions[directionkey]
        for i in range(n):
            pa += dpa
            pb += dpb
            pc += dpc
            val += 1
            answers.append((pa, pb, pc, val))
            
        n -= 1
        directionkey = (directionkey + 1)%3
        
    # sort
    answer = []
    answers.sort()
    for a in answers:
        answer.append(a[-1])
    
    return answer