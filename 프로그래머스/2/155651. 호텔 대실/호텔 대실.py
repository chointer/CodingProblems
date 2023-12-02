# n <= 1e3
# 한 번에 가장 많은 객실이 요구되는 때의 객실 수?
# Pointer

from collections import deque

def str2int(times):
    answer = []
    for t in times:
        t = t.split(':')
        answer.append(int(t[0])*60 + int(t[1]))
    return answer

def solution(book_time):
    in_times, out_times = [], []
    
    for b_time in book_time:
        st, en = str2int(b_time)
        in_times.append(st)
        out_times.append(en + 10)
    
    in_times.sort()
    out_times.sort()
    in_times = deque(in_times)
    out_times = deque(out_times)
    
    rooms_max = 0
    rooms_current = 0
    while in_times:
        if out_times and in_times[0] >= out_times[0]:
            out_times.popleft()
            rooms_current -= 1
        else:
            in_times.popleft()
            rooms_current += 1
            if rooms_max < rooms_current:
                rooms_max = rooms_current
    
    return rooms_max