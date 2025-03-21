# 1e6. 1) 첫 집을 터는 경우: 마지막 집 제거, 2) 첫 집을 털지 않는 경우: 마지막 집 유지
# i-th 집을 터는 경우의 최댓값 = f(i) + max( dp(i - 2), dp(i - 3) )

def solution(money):
    dp = [money[0], max(money[0], money[1]), max(money[0] + money[1], money[2])]    
    if len(money) == 3:
        return max(dp)
    
    # 1) 마지막 집을 털면 안되는 경우, // dp = [m1, max(m1, m2), ...]
    dp1 = [money[0], money[1], max(money[0] + money[2], money[1])]    
    for i, mon in enumerate(money[3:-1], start=3):
        dp1.append(mon + max(dp1[i - 2], dp1[i - 3]))
    
    # 2) 마지막 집을 털어도 되는 경우,
    dp2 = [0, money[1], money[2]]
    for i, mon in enumerate(money[3:], start=3):
        dp2.append(mon + max(dp2[i - 2], dp2[i - 3]))
    
    return max(dp1 + dp2)