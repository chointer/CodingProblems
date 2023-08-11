from collections import deque
def solution(s):
    s = deque(s)
    count = 0
    x = ''
    while(s):
        if not x:
            x = s.popleft()
            nx, nnx = 1, 0
        else:
            now = s.popleft()
            if now == x:
                nx += 1
            else:
                nnx += 1
            if nx == nnx:
                count += 1
                x = ''
    
    return count if not x else count + 1