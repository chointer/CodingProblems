# DP?
# 아이디어가 떠오르지 않아서 답 확인함. DP인데, 경우를 여러 개로 나누어야 하는 것이었다. 
# 기본적으로는 unit(돈 단위)만큼 이전의 경우의 수를 unit에 대해 모두 더하면 되지만,
# 중복되는 경우가 있어서 문제가 된다.
# 어떤 unit에 대해, (N-unit)원 거슬러주는 경우 중에서 unit보다 작은 단위가 있는 경우를 제외한 경우들을 모두 더한다.(중복 방지) -> N원을 거슬러주는 경우 중, 최소단위가 unit인 경우들이 된다.
# 단위가 [2, 3, 5]이고, 9원을 거슬러 줄 때, 7, 6, 4원을 거슬러 주는 경우를 고려하는데, 7원은 최소 단위가 2 이상인 경우(사실 모든 경우)를, 6원은 최소 단위가 3 이상, 4원은 최소 단위 5 이상인 경우만을 더해준다.
# 다만, 시간 초과가 발생한다고 한다. 그래서 i원 거스르는 경우를 구할 때, 모든 경우의 수를 더한 값(sum)을 저장한다. 이후에 조금씩 사용하는 개념으로 빼준다; i+unit 계산 시, sum을 이용하고, i원 경우 중 unit 이상 단위로만 구성된 경우의 수를 뺀다. 다음 계산에서는 그 값이 unit_next 이상 단위로만 구성된 경우의 수가 될 것이기 때문이다.
# 너무 어렵다!

def solution(n, money):
    money.sort()
    dp = [[0 for _ in range(len(money))] for _ in range(n)]
    dp_t = [0 for _ in range(n)]
    
    for i, unit in enumerate(money):
        if unit > n: continue
        dp[unit-1][i] = 1
        dp_t[unit-1] = 1
    
    for num in range(n):         # case of (num+1)
        # ((num+1)-unit)원에 대해, 최소단위가 unit인 경우 처리
        for u_idx, unit in enumerate(money):
            if num - unit >= 0:
                dp[num][u_idx] = dp_t[num - unit]
                dp_t[num - unit] -= dp[num - unit][u_idx]
                dp_t[num] += dp[num][u_idx] % 1000000007
    
    return dp_t[-1]