# N <= 1e3, H <= 1e4
def solution(citations):
    citations.sort(reverse=True)
    
    for i, h in enumerate(citations, start=1):
        if h < i:
            return i - 1
    else:
        return i












"""
from collections import Counter

def solution(citations):
    N_high = 0
    cite_dict = Counter(citations)

    for i in range(max(citations), 0, -1):
        N_high += cite_dict[i]
        if N_high >= i:
            return i
    return 0
"""