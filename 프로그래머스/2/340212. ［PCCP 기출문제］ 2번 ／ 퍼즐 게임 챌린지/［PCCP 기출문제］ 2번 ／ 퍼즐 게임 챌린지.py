# n개 퍼즐, 퍼즐 난이도 diff, 숙련도 level.   
# (Level은 1 이상이고, 0번째 퍼즐은 항상 난이도 1이라 틀릴 일이 없다.)
# 이진 탐색?
# diff <= 1e5, level에 따른 소요 시간 계산 O(N) = N_puzzle <= 1e5
# level 범위는 1e5이므로 모든 탐색은 불가능. 이진 탐색 맞을 듯


def cal_time(level, diffs, times):
    total_time = 0
    
    time_prev = 0
    for diff, time_cur in zip(diffs, times):
        level_gap = diff - level
        total_time += max(level_gap, 0) * (time_prev + time_cur) + time_cur
        time_prev = time_cur
        
    return total_time
        
        
def solution(diffs, times, limit):
    st = 1
    en = 100000
    
    while st <= en:
        mid = (st + en) // 2
        t = cal_time(mid, diffs, times)
        
        if t > limit:
            st = mid + 1
        
        else:       # t <= limit:
            en = mid - 1
        
    return st