# DFS? 어렵다!
# 각 점수에서 2가지 선택. -> 2**10 ~ 10**3

def compare(A, B):
    if A[0] > B[0]:
        return A
    elif A[0] < B[0]:
        return B
    else:
        for i in range(-1, -10, -1):
            if A[i] > B[i]:
                return A
            elif A[i] < B[i]:
                return B
    return A


def subsol(Lion_Pro, Apeach_Post, n_left, score_Lion, score_Apeach, Lion_best):
    if n_left < 0:
        return Lion_best
    
    if not Apeach_Post:
        if score_Lion > score_Apeach:
            return compare([score_Lion - score_Apeach] + Lion_Pro + [n_left], Lion_best)
            
        else:
            return Lion_best
        
    # 겨우 이기는 경우; Apeach[0] + 1
    n_shot = Apeach_Post[0] + 1
    if n_left >= n_shot:
        score_Add = len(Apeach_Post)
        if Apeach_Post[0] != 0: 
            Lion_best = subsol(Lion_Pro + [n_shot], Apeach_Post[1:], n_left - n_shot, score_Lion+score_Add, score_Apeach-score_Add, Lion_best)
        else:
            Lion_best = subsol(Lion_Pro + [n_shot], Apeach_Post[1:], n_left - n_shot, score_Lion+score_Add, score_Apeach, Lion_best)
        
    # 완전 포기하는 경우; 0
    best2 = subsol(Lion_Pro + [0], Apeach_Post[1:], n_left, score_Lion, score_Apeach, Lion_best)
    
    return compare(Lion_best, best2)
    
    
    
def solution(n, info):
    # Calculate Apeach's Score
    score_Apeach = 0
    for i, a in enumerate(info):
        if a != 0:
            score_Apeach += 10-i
    
    # DFS
    Lion = []
    best = subsol(Lion, info[:-1], n, 0, score_Apeach, [-score_Apeach, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n])
    print(best)
    if best[0] <= 0:
        return [-1]

    return best[1:]