# 경계 상황에 대한 고려가 부족했다.

from collections import deque
import heapq

def solution(n, k, enemy):
    saver = []
    answer = k
    enemy = deque(enemy)
    
    for i in range(k):
        heapq.heappush(saver, enemy.popleft())
        if not enemy: 
            return i + 1
    
    while n >= 0 and enemy:
        enemy_this_round = enemy.popleft()
        if enemy_this_round > saver[0]:
            n -= heapq.heappop(saver)
            heapq.heappush(saver, enemy_this_round)
        else:
            n -= enemy_this_round
        answer += 1

    return answer - 1 if n < 0 else answer