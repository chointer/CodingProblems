# s <= 1e5
# 1. '('가 +1, ')' -1일 때, 음수가 되면 안된다.
# 2. 확인이 끝난 뒤에 0이 아니면 안된다.

def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
        
    return False if count != 0 else True
            
        
    
    
    
    
    
    

"""
def solution(s):
    l = 0
    for i in s:
        if i == '(':
            l += 1
        else:
            l -= 1
        if l < 0:
            return False
    if l == 0:
        return True
    else:
        return False
"""