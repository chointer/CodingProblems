# n <= 1e9, 심사관 <= 1e6
# 시간의 최솟값.
# n * time <= 1e18
# log (n*time) ~60 * 1e6
# log (n*time) * n2 + n2 log n2

def is_possible(t, n, times):
    for tim in times:
        n -= t // tim
        if n <= 0:
            return True
    return False if n > 0 else True

def solution(n, times):
    times.sort()
    
    st = 0
    en = 10**18 + 1
    
    while st <= en:
        mid = (st + en) // 2
        ispossible = is_possible(mid, n, times)
        if ispossible:
            en = mid - 1
        else:
            st = mid + 1
    
    return st