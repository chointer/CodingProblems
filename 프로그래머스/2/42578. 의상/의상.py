from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for c in clothes:
        clothes_dict[c[1]] += 1
    
    answer = 1
    for v in clothes_dict.values():
        answer *= (v + 1)
        
    return answer - 1