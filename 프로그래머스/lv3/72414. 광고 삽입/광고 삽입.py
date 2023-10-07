# time(3.6*1e5), log(3*1e5)
# Two Pointer?

import heapq
from collections import deque

def str2int(time):
    h, m, s = time.split(':')
    return int(s) + 60 * (int(m) + 60 * int(h))

def int2str(time):
    s = time%60
    time = time//60
    m = time%60
    h = time//60
    return '{0:0>2}:{1:0>2}:{2:0>2}'.format(h, m, s)

def solution(play_time, adv_time, logs):
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    
    # Make logs as a list
    log_seq = []
    log_seq_p1 = deque([])
    for log in logs:
        st, en = log.split('-')
        st = str2int(st)
        en = str2int(en)
        
        heapq.heappush(log_seq, (st, 1))
        heapq.heappush(log_seq, (en, -1))
    

    p1 = -adv_time
    p2 = 0
    p1_viewers = 0
    p2_viewers = 0
    stack_time = 0
    p_max = p1
    stack_time_max = 0
    
    while p2 <= play_time:
        while log_seq and log_seq[0][0] == p2:
            ti, sign = heapq.heappop(log_seq)
            log_seq_p1.append((ti, sign))
            p2_viewers += sign
        while log_seq_p1 and log_seq_p1[0][0] == p1:
            _, sign = log_seq_p1.popleft()
            p1_viewers += sign
        
        stack_time -= p1_viewers
        stack_time += p2_viewers
        if p1 >= 0 and stack_time_max < stack_time:
            stack_time_max = stack_time
            p_max = p1
        p1 += 1
        p2 += 1
        
    return int2str(p_max + 1) if p_max != 0 else int2str(p_max)