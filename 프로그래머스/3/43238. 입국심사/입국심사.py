# n <= 1e9, checker <= 1e5
# sum(t 시간동안 각 심사관이 심사할 수 있는 사람 수)를 binary search.

def screening(k, times):
    people = 0
    for t in times:
        people += k//t
    return people

def solution(n, times):
    st = 0
    en = max(times) * n
    
    while st <= en:
        mid = (st + en) // 2
        n_in_t = screening(mid, times)
        
        if n <= n_in_t:
            en = mid - 1
        else:
            st = mid + 1
    
    return st
        
    answer = 0
    return answer