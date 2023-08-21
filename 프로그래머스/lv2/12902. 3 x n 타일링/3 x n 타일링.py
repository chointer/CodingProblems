# DP
# n=2 제외, 경계가 나누어지지 않으면서 n을 채우는 방법은 2가지
# 홀수 n은 불가능
# f(n) = f(n-2) * 3 + { f(n-4) * 2 + f(n-6) * 2 + ... } + 2
# = 2 * { f(n-2) + f(n-4) ... } + f(n-2) + 2
# = 2 * f_sum(n-2) + f(n-2) + 2
# f_sum(n) = f_sum(n-2) + f(n)

def solution(n):
    if n%2==1: return 0
    fn = {2: 3}
    fsum = {2: 3}
    
    n0 = 2
    while n0 <= n:
        n1 = n0 + 2
        fn[n1] = (fsum[n0] * 2 + fn[n0] + 2) % 1000000007
        fsum[n1] = fsum[n0] + fn[n1]
        n0 = n1

    return fn[n]