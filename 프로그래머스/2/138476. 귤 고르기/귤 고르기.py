# 귤 크기 <= 1e7, 귤 개수 <= 1e5

from collections import Counter

def solution(k, tangerine):
    stat = Counter(tangerine)
    num_lis = []
    for num in stat.values():
        num_lis.append(num)
    num_lis.sort(reverse=True)

    idx = 0
    while k > 0:
        k -= num_lis[idx]
        idx += 1
    
    return idx