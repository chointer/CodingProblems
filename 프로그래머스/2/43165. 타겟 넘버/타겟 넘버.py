from collections import deque
def solution(numbers, target):
    answer = 0
    N = len(numbers)
    q = deque([(0, 0)])         # (current, idx_next)
    
    while q:
        current, idx_next = q.popleft()
        
        if idx_next == N:
            if current == target:
                answer += 1
            continue
        
        q.append((current + numbers[idx_next], idx_next + 1))
        q.append((current - numbers[idx_next], idx_next + 1))
    
    return answer