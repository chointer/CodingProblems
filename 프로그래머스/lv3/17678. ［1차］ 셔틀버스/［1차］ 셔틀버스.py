# 직원 <= 2000, 버스 <= 10
# 마지막 버스보다 늦은 직원은 생각하지 않는다.
# 버스를 타는 직원들 중, 마지막 버스 도착 시각에 타보고, 안된다.-> 마지막 직원보다 바로 앞?

from collections import deque

def str2int(time):
    h,m = time.split(":")
    return 60*int(h) + int(m)

def int2str(time):
    h = str(time//60)
    h = h if len(h) == 2 else '0' + h
    m = str(time%60)
    m = m if len(m) == 2 else '0' + m
    return h + ':' + m

def solution(n, t, m, timetable):
    timetable = deque([str2int(ti) for ti in sorted(timetable)])

    t0 = str2int("09:00")
    for arrive in range(t0, t0 + t*n, t):
        n_in_bus = 0                            # 버스 탑승 인원
        while timetable and (timetable[0] <= arrive) and (n_in_bus < m):
            last_crew = timetable.popleft()
            n_in_bus += 1
    
    if n_in_bus == m:
        answer = last_crew - 1
    else:
        answer = arrive
    
    return int2str(answer)