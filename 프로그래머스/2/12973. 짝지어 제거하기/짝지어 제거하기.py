# s <= 1e6
from collections import deque
def solution(s):
    stack = []
    s = deque(s)
    
    while s:
        current_letter = s.popleft()
        if stack and stack[-1] == current_letter:
            stack.pop()
        else:
            stack.append(current_letter)
        
    return 0 if stack else 1