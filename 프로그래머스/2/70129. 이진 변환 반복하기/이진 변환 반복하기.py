# N < 2e5

def transform(s):
    count_1 = 0
    for i in s:
        if i == '1':
            count_1 += 1
    return bin(count_1)[2:], len(s) - count_1

def solution(s):
    count_0 = 0
    count_tr = 0
    
    while s != '1':
        s, removed_0 = transform(s)
        count_tr += 1
        count_0 += removed_0
    
    return [count_tr, count_0]