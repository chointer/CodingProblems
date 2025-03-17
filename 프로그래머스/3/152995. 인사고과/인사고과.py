# 못풀었음! 옛날엔 풀었던가..
# 오름차순 내림차순

def solution(scores):
    my_score = scores[0]
    my_score_sum = sum(my_score)
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    max_score_2 = -1
    rank = 0
    
    for score in scores:
        # reject check
        if max_score_2 <= score[1]:
            max_score_2 = score[1]
        else:
            if score == my_score:
                return -1
            continue
        
        # compare with my_score
        if sum(score) > my_score_sum:
            rank += 1
    
    return rank + 1