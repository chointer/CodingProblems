import heapq as hq
from collections import deque

# N <= 500
# 우선 순위: (소요 시간, 요청 시각, 작업 번호)
# t 시점,
# 1. t 시점까지의 jobs(deque)에서 job을 대기열(heapq)에 추가한다.
# 2. 최우선 작업을 대기열에서 하나 꺼내서 수행한다.
#   2-1. 대기열에 작업이 없으면, jobs[0]의 시점으로 t를 갱신한다.
# 3. 수행한 작업 반환 시간을 계산하고, 끝난 시각으로 t를 갱신한다.

def solution(jobs):
    turntimes = []
    waits = []
    jobs = [(l, s, i) for i, (s, l) in enumerate(jobs)]
    jobs = sorted(jobs, key=lambda x: x[1])
    jobs = deque(jobs)
    t = 0

    while jobs or waits:
        while jobs and jobs[0][1] <= t:
            hq.heappush(waits, jobs.popleft())

        if waits:
            length, start, _ = hq.heappop(waits)
            t += length
            turntimes.append(t - start)
        else:
            t = jobs[0][1]

    return sum(turntimes)//len(turntimes)
    

"""
import heapq
from collections import deque

def solution(jobs):
    q = []                  # delayed works
    N = len(jobs)
    jobs.sort()
    jobs = deque(jobs)
    print(jobs)
    
    t = 0
    t_work = 0
    while jobs or q:
        if q:
            work = heapq.heappop(q)
            work = (work[1], work[0])
        else:
            work = jobs.popleft()
            t = work[0]
        
        t += work[1]
        t_work += t - work[0]
        
        while jobs and jobs[0][0] < t:
            delay = jobs.popleft()
            heapq.heappush(q, (delay[1], delay[0]))
    return t_work//N
"""