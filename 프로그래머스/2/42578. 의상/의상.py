# N <= 30
# 시간 초과가 하나 발생했다. combinations를 반복해서 사용했는데, 안입는 경우를 추가해서 경우의 수를 구하면 간단해진다...

from collections import Counter

def solution(clothes):
    counter = Counter([cloth[1] for cloth in clothes])
    
    count = 1
    
    for i in counter.values():
        count *= i + 1
            
    return count - 1
    
    
"""def solution(clothes):
    clo_dict = {}
    for name, clo in clothes:
        if clo in clo_dict:
            clo_dict[clo] += 1
        else:
            clo_dict[clo] = 1
    
    answer = 1
    for key in clo_dict.keys():
        answer *= (clo_dict[key] + 1)
        
    return answer - 1
"""