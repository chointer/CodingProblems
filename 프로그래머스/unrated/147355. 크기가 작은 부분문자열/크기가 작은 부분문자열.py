# deque      O(2*nt*np)? -> O(nt*np) < 10^6
# slicing    O(np*nt*np)? -> O(nt*np) < 10^8

from collections import deque

def solution(t, p):
    np = len(p)
    compare = deque(t[:np-1], maxlen=np)
    
    count = 0
    for s in t[np-1:]:
        compare.append(s)
        if "".join(compare) <= p:
            count += 1
            
    return count