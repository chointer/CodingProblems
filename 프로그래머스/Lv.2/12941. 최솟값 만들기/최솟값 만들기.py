# N <= 1e3
# 단순 모든 경우의 수? ~1e6
# a1 >= a2, b1 >= b2
# a1(b1-b2) + a2(b2-b1) = (a1-a2)(b1-b2) >= 0
# a1b1 + a2b2 >= a1b2 + a2b1
# 큰 것끼리 더하는게 더 크다.

def solution(A, B):
    A.sort(reverse=True)
    B.sort()
    answer = sum(a*b for a, b in zip(A, B))
    return answer