# 가장 많이 남은 작업을 하는 것이 최선의 선택일 것이다.
# 1시간동안 가장 많이 남은 작업과 다른 작업을 했을 때, 
# 야근 피도로의 감소량은 가장 많이 남은 작업을 했을 때 가장 크기 때문 (미분처럼)
# binary search..?

import heapq

def find_n(works, work_max):
    result = 0
    for work in works:
        result += max(0, work - work_max)
    return result

def cut_works(works, work_max):
    result = []
    for work in works:
        result.append(min(work, work_max))
    return result

def cal_idx(left_works):
    result = 0
    for work in left_works:
        result += work**2
    return result

def solution(n, works):
    st = 0              # n = max
    en = 50000          # n = 0
    
    while st < en:
        mid = (st + en)//2
        nn = find_n(works, mid)
        if nn < n:    # -> lower mid (work_max)
            en = mid
        elif nn > n:
            st = mid + 1
        else:
            return cal_idx(cut_works(works, mid))
    
    # st==en
    left_n = n - find_n(works, st)
    left_works = cut_works(works, st)

    left_works_ = [-i for i in left_works]
    heapq.heapify(left_works_)
    
    for i in range(left_n):
        if left_works[0] == 0:
            break
        a = heapq.heappop(left_works_) + 1
        print(a)
        heapq.heappush(left_works_, a)
        
    print(left_works_)
    return cal_idx([-i for i in left_works_])