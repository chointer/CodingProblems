# n < 1e4, s < 1e8
# 그냥 s/n 값 기반으로 할까

def solution(n, s):
    base = s//n
    left = s%n
    if base == 0: return [-1]
    
    answer = [base for i in range(n)]
    for i in range(left):
        answer[-(i + 1)] += 1

    return answer