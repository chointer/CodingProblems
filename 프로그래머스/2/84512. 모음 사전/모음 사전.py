# 5진수로 표현하면 편한가? 없는 문자에 대한 처리가 애매하다.
# 완탐이네. N(word) <= 5. 가짓 수 < 6**5 < 8000
# DFS로 해야하네. stack
# 문자열 비효율적이지만 일단 관리가 편하므로 문자열로 해보기.

def solution(word):
    aeiou = ["U", "O", "I", "E", "A"]
    stack = [i for i in aeiou]
        
    idx = 1
    while stack:
        w = stack.pop()
        if w == word:
            break
        
        idx += 1
        if len(w) < 5:
            for i in aeiou:
                stack.append(w + i)
        
    return idx