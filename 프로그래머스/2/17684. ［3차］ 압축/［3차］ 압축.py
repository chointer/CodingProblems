# L <= 1e3

from collections import deque
def solution(msg):
    di = {s: i + 1 for i, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    next_idx = 27
    idx = 0
    buffer = ""
    
    answer = []
    msg = deque(msg)
    while msg:
        s = msg.popleft()
        buffer += s
        
        if buffer in di:
            idx = di[buffer]
            
        else:
            answer.append(idx)
            di[buffer] = next_idx
            next_idx += 1
            buffer = buffer[-1]
            idx = di[buffer]
    
    answer.append(di[buffer])
    
    return answer