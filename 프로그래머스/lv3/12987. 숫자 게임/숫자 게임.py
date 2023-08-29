# B에서 가장 높은 숫자 순서대로 A를 이기는 가장 큰 수와 매칭. Greedy?
# 7m 0s
def solution(A, B):
    B.sort()
    A.sort()
    score = 0
    
    while A:
        if A.pop() < B[-1]:
            B.pop()
            score += 1
    return score