def solution(arr):
    idx = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    print(idx)
    if len(idx) >= 2:
        return arr[idx[0]:idx[-1] + 1]
    
    elif len(idx) == 1:
        return [2]
    
    else:
        return [-1]