from collections import deque

def solution(n, m, section):
    section = deque(section)
    count = 0
    
    while section:
        now = section.popleft()
        lim = now + m
        count += 1
        
        while section and section[0] < lim:
            section.popleft()
        
    return count