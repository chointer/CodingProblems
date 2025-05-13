# k <= 5e3, dungeons <= 8

from itertools import permutations

def solution(k, dungeons):
    max_i = 0
    
    for seq in permutations(dungeons):
        l = k
        i = 0
        for min_req, use in seq:
            if l >= min_req:
                i += 1
                l -= use
            else:
                break
            max_i = max(max_i, i)

    
    return max_i
                
            
            

"""
from itertools import permutations

def dungeoning(k, dungeons):
    done = 0
    for dungeon in dungeons:
        low, cost = dungeon
        if low <= k:
            k -= cost
            done += 1
        else:
            break
    return done
    
def solution(k, dungeons):
    d_max = 0
    for dgs in permutations(dungeons):
        d = dungeoning(k, dgs)
        if d_max < d:
            d_max = d
    
    return d_max
"""