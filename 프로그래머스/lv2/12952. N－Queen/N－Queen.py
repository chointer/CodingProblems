# DFS or DP?
# 실제 체스판을 만들어 경우를 기록하지 말고,
# 배치한 위치를 기반으로 가능한지 아닌지를 체크하면 속도가 더 빠를 것 같다. -> 시간 초과 (12에서만 걸리는 듯)
# 힌트: 백트래킹 (규칙을 찾아 조건을 줄이라고 함.)
# 처음에 n/2까지만 탐색하여 시간을 절반으로 줄인다. 
# n이 짝수이면, 첫 줄 n/2까지 탐색, 반전을 고려하여 *2 해준다.
# n이 홀수인 경우, 첫 줄 n/2보다 작을 때 퀸이 배치된 경우는 반전을 고려하여 *2를 해주지만,
#       첫 줄 가운데에 퀸을 배치할 때는 모든 경우를 탐색하게 되므로 *2를 해주면 안 된다.

Queens = []

def available(y, x):
    result = True
    for Queen in Queens:
        if y == Queen[0] or x == Queen[1] or x + y == Queen[2] or x-y == Queen[3]:
            result = False
    return result
    
def subsol(now, n):
    # Queens: a list composed of (y, x, x+y, x-y)
    # now: 현재 퀸을 놓을 row index
    if now == n:
        return 1
    
    count = 0
    
    for i in range(n):
        # maps[now][i]
        if now == 0 and i >= n/2: 
            continue
        if available(now, i):
            Queens.append((now, i, now+i, i-now))
            count += subsol(now+1, n)
            Queens.pop()

    return count
            

        
def solution(n):
    count = 0
    for i in range(n//2):
        Queens.append((0, i, i, i))
        count += subsol(1, n)
        Queens.pop()
    count *= 2
    
    if n%2 == 1:
        i = n//2
        Queens.append((0, i, i, i))
        count += subsol(1, n)
    return count
