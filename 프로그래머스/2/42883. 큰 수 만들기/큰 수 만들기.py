# n: 1e6 자리수
# 하나씩 지운다. 
# first minimum을 지운다. 다음 요소가 더 크면, 지운 다음, 직전 요소와 다음 요소를 비교한다.
# 직전 요소가 없는 경우와 다음 요소가 없는 경우 체크하기

from collections import deque

def solution(number, k):
    stack = [number[0]]
    queue = deque(number[1:])
    
    while queue and k > 0:
        if not stack:
            stack.append(queue.popleft())
            continue
        
        elif stack[-1] < queue[0]:
            stack.pop()
            k -= 1
        
        else:
            stack.append(queue.popleft())
    
    answer = "".join(stack + list(queue))
    return answer if k == 0 else answer[:-k]