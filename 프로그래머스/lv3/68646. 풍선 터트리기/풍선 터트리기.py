# 평면에서 생각하니 규칙 찾기가 편했다.
# 생각보다 구현 오래 걸렸음.
# 반대로 생각해서 틀림.

def solution(a):
    MAX = 1000000001
    L_min = [MAX]
    for i in a:
        L_min.append(min(L_min[-1], i))
    L_min = L_min[:-1]
    
    R_min = [MAX]
    for i in a[::-1]:
        R_min.append(min(R_min[-1], i))
    R_min = R_min[::-1][1:]
    
    count = 0
    for L, mid, R in zip(L_min, a, R_min):
        if mid < L or mid < R:
            count += 1
    
    return count