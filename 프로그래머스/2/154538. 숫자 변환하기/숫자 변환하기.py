# x + n
# x * 2
# x * 3
# x, y < 1e6
# DP; 어떤 수를 만들기 위한 최소 연산 횟수

def find(t, n, sols):
    answer = 10000000
    if t - n >= 0 and sols[t - n] is not None:
        answer = min(answer, sols[t - n] + 1)
    
    if t%2 == 0 and sols[t//2] is not None:
        answer = min(answer, sols[t//2] + 1)
        
    if t%3 == 0 and sols[t//3] is not None:
        answer = min(answer, sols[t//3] + 1)
    
    return answer if answer != 10000000 else None

        
def solution(x, y, n):
    sols = [None for i in range(y + 1)]
    sols[x] = 0
    
    for i in range(x + 1, y + 1):
        sols[i] = find(i, n, sols)

    return sols[-1] if sols[-1] is not None else -1