# No duplicate number
# The number that has been pointed out cannot be pointed out again.
# Each step ends forming a cycle.

from collections import Counter

def solution(cards):
    roots = [0 for i in range(len(cards) + 1)]
    cards = [0] + cards
    tag = 1
        
    for i in range(1, len(roots)):
        if roots[i] != 0: continue

        while roots[i] == 0:
            roots[i] = tag
            i = cards[i]
        tag += 1    
    
    counts = Counter(roots[1:])
    scores = sorted(counts.values(), reverse=True)

    return 0 if len(scores) == 1 else scores[0]*scores[1]