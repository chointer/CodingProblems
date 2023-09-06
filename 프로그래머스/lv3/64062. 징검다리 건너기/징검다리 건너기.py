# 배열 크기2*1e5/ 원소 범위 2*1e8
# binary search?
# one search O ~ 1e5
# max search O ~ log 1e8
# ~ 1e6?

def check(stones, k, n):
    count = 0
    for stone in stones:
        if stone >= n:
            count = 0
        else:
            count += 1
            if count >= k:
                return False
    return True
    
def solution(stones, k):
    st = 1
    en = 200000000
    
    while True:
        mid = (st + en) // 2
        if mid == st:
            break
        if check(stones, k, mid):       # True -> 더 큰 값 확인
            st = mid
        else:
            en = mid
            
    return mid