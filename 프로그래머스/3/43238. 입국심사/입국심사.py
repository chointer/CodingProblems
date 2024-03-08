# N <= 1e9. 심사관 <= 1e5

def is_possible(t, n, times):
    n_max = 0
    for ti in times:
        n_max += t//ti
    return n_max >= n

def solution(n, times):
    st = 0
    en = n * min(times)
    
    while st < en:
        mid = (st + en) // 2
        if is_possible(mid, n, times):
            en = mid
        else:
            st = mid + 1

    return st