# N <= 500.
# 항상 짧은 것 먼저하는 것이 낫다.
# 2개의 요청이 대기중 일 때, 
# 각 요청의 지금까지의 대기 시간과 수행 시간을 각각 x0 + x > y0 + y 이라 하면,
# x 후 y: x0 + x + y0 + x + y
# y 후 x: x0 + y + x + y0 + y
# 비교하면 1번째 방법이 y - x 만큼 더 빠르다.

import heapq
from collections import deque

def solution(jobs):
    N = len(jobs)
    jobs = deque(sorted(jobs))
    tasks = []
    t_done = 0
    t_work = 0
    
    while jobs or tasks:
        if not jobs and not tasks:
            break
            
        # 작업이 없으면 무조건 다음 작업 받기
        if not tasks:
            t0, t = jobs.popleft()
            heapq.heappush(tasks, (t, t0))
            t_done = t0
        
        # 작업 선택 수행
        t, t0 = heapq.heappop(tasks)
        t_done += t
        t_work += t_done - t0
            
        # 현 작업을 마칠 때까지 job 받기
        while jobs and jobs[0][0] <= t_done:
            t0, t = jobs.popleft()
            heapq.heappush(tasks, (t, t0))
    
    return t_work//N