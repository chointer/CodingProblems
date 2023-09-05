from collections import deque

def solution(gems):
    N = len(set(gems))
    buy_list = deque()
    buy_counts = {i:0 for i in set(gems)}
    category_num = 0
    answer = (0, 100000)
    
    st = 0
    for en, gem in enumerate(gems):
        buy_list.append(gem)
        if buy_counts[gem] == 0:
            category_num += 1
        buy_counts[gem] += 1
        
        while buy_counts[buy_list[0]] > 1:
            buy_counts[buy_list.popleft()] -= 1
            st += 1
            
        if category_num == N:
            if answer[1] - answer[0] > en - st:
                answer = (st, en)
            
    return [answer[0] + 1, answer[1] + 1]