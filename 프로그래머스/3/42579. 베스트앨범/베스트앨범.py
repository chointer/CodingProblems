# 장르별로 (번호, 재생 수)
from collections import defaultdict

def solution(genres, plays):
    total_plays = defaultdict(int)
    id_and_plays = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        total_plays[genre] += play
        id_and_plays[genre].append((play, i))
    
    total_plays = sorted([(v, k) for k, v in total_plays.items()], reverse=True)
    total_plays = [element[1] for element in total_plays]
    
    answer = []
    for genre in total_plays:
        element_id_play = sorted(id_and_plays[genre], key=lambda x: (-x[0], x[1]))
        for i in range(min(len(element_id_play), 2)):
            answer.append(element_id_play[i][1])
            
    return answer
                                 
        
    

"""
def solution(genres, plays):
    gen_play = {}   # gen: (play, id)
    gen_cnt = {}    # gen: cnt
    
    for i in set(genres):
        gen_play[i] = []
        gen_cnt[i] = 0
        
    for i in range(len(genres)):
        gen_play[genres[i]].append((-plays[i], i))
        gen_cnt[genres[i]] += plays[i]
        
    gen_order = []
    for i in gen_cnt.keys():
        gen_play[i].sort()
        gen_order.append((gen_cnt[i], i))
    gen_order.sort(reverse=True)
    
    answer = []
    for _, gen in gen_order:
        answer.append(gen_play[gen][0][1])
        if len(gen_play[gen]) > 1:
            answer.append(gen_play[gen][1][1])
    
    
    
    return answer
"""