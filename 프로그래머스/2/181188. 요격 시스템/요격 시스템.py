# N <= 5e5, range <= 1e8
# Greedy. 
# 하나의 폭격에 대해서는 반드시 최소 하나의 요격이 필요하다.
# 가장 끝의 폭격부터, 가장 많이 요격할 수 있도록한다.
# O = NlogN + N

def solution(targets):
    count = 1
    left = 0
    right = 100000000
    
    for st, en in sorted(targets):
        if st < right: # en > left
            left = max(left, st)
            right = min(right, en)
        else:
            count += 1
            left = st
            right = en
    
    return count