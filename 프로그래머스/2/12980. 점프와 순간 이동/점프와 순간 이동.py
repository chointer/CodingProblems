# N <= 1e9
# 어렵다. DP? BS?
# Greedy? 이진수?
def solution(n):
    ans = 0
    for i in bin(n)[2:]:
        if i == '1': ans += 1
    return ans