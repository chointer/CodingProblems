# max count: max(t) * max(m) = 10**5
# 32m
from collections import deque

def d2n(num, n):
    result = []
    while num != 0:
        result.append(hex(num%n)[2:].upper())
        num //= n
    return deque(result[::-1])

def solution(n, t, m, p):
    num = 0
    num_str = deque(['0'])
    order = 0
    answer = []
    p -= 1
    
    for i in range(t):
        
        # not Tube's Turn
        while order%m != p:
            if not num_str:
                num += 1
                num_str = d2n(num, n)      # fix
            num_str.popleft()
            order += 1
        
        # Tube's Turn
        if not num_str:
            num += 1
            num_str = d2n(num, n)
        answer.append(num_str.popleft())
        order += 1
        
    return "".join(answer)