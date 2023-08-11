def solution(s):
    l = len(s)
    if l != 4 and l != 6:
        return False
    
    for i in s:
        if i not in "0123456789":
            return False
    
    return True
        