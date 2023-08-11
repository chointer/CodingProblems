from collections import Counter


def solution(topping):
    # left idx
    st = 0
    en = len(topping) - 1
    mid = (st+en)//2
    
    while st < mid:
        print(st,mid,en,'left')
        le = len(set(topping[:mid]))
        ri = len(set(topping[mid:]))

        if le < ri: st = mid
        else: en = mid              # le >= ri
        mid = (st+en)//2
    
    le = len(set(topping[:mid]))
    ri = len(set(topping[mid:]))
    if le < ri:
        idx_left = mid + 1
    else:
        idx_left = mid
    
    
    # right idx
    st = 0
    en = len(topping) - 1
    mid = (st+en)//2
    
    while st < mid:
        print(st,mid,en)
        le = len(set(topping[:mid]))
        ri = len(set(topping[mid:]))

        if le <= ri: st = mid
        else: en = mid              # le > ri
        mid = (st+en)//2
        
    mid += 1
    
    le = len(set(topping[:mid]))
    ri = len(set(topping[mid:]))
    if le <= ri:
        idx_right = mid
    else:
        idx_right = mid - 1

    return 0 if idx_right < idx_left else idx_right - idx_left + 1