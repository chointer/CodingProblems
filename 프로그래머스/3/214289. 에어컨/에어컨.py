# 냉방과 난방은 음수를 곱해서 방향을 같게 만들자.
# DP를 쓰라는 힌트를 봤다. 그런데 어떻게? 2차원으로 하는구나... 흑흑
#       => "dp[i][j]는 현재 i분, 온도 j에 도달할 수 있는 최소 전력"이라고 한다.
# time <= 1000

def solution(temperature, t1, t2, a, b, onboard):
    if temperature < t1:                        # heating mode -> cooling
        temperature, t1, t2 = -temperature, -t2, -t1
    
    dp = [{} for _ in range(len(onboard))]
    dp[0][temperature] = 0

    # no use: (temp + 1) or temperature, cost
    # down: temp - 1, cost + a
    # maintain: temp, cost + b
    cases = [(1, 0), (-1, a), (0, b)]
    
    for i, board in enumerate(onboard[:-1]):
        for t, c in dp[i].items():
            if board and (t < t1 or t > t2):
                continue
            for dt, dc in cases:
                t_next = t + dt
                c_next = c + dc
                if dt == 1 and t == temperature:
                    t_next = t
                
                if t_next in dp[i + 1]:
                    dp[i + 1][t_next] = min(dp[i + 1][t_next], c_next)
                else: dp[i + 1][t_next] = c_next
    
    min_cost = max(a, b) * len(onboard)
    for t, c in dp[-1].items():
        if onboard[-1] and (t < t1 or t > t2):
            continue
        min_cost = min(min_cost, c)
    
    return min_cost