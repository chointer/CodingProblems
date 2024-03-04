# N <= 1e4
def solution(answers):
    p1, p2, p3 = 0, 0, 0
    ref2 = [1, 3, 4, 5]
    ref3 = [3, 1, 2, 4, 5]
    
    for i, ans in enumerate(answers):
        if i%5 + 1 == ans:
            p1 += 1
        
        if i%2 == 0 and ans == 2:
            p2 += 1
        elif i%2 == 1 and ans == ref2[(i//2)%4]:
            p2 += 1
    
        if ans == ref3[((i//2)%5)]:
            p3 += 1
    
    scores = [p1, p2, p3]
    best_score = max(scores)
    answer = []
    for i, score in enumerate(scores):
        if score == best_score:
            answer.append(i + 1)
            
    return answer