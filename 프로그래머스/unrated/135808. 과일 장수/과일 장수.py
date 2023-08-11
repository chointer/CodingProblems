# 낮은 점수끼리 모아둔다. -> 낮은 가격 박스 최소화
from collections import Counter

def solution(k, m, score):
    scores = Counter(score)
    
    answer = 0
    left = 0
    for i in range(k, 0, -1):
        n = scores[i] + left
        answer += n//m * i * m
        left = n%m
        
    return answer