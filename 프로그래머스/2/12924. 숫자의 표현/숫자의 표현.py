# 0 < n < 1e4
# 2 pointers
# idx1 이상, idx2 미만. O(N)

def solution(n):
    st = 1
    en = 1
    temp_sum = 1
    count = 0
    if n == 1: return 1

    while en <= n:
        if temp_sum < n:
            en += 1
            temp_sum += en
        elif temp_sum == n:
            count += 1
            en += 1
            temp_sum += en
        else:   # temp_sum > n
            temp_sum -= st
            st += 1
    
    return count