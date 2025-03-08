# len(s) = 1e3
# 1e3번 체크? 체크 당, 1e3번 해야해서, 시간복잡도는 충분해보인다. stack으로 구현?
# 올바른 문자열이 있을 때, 덩어리 개수만큼 가능한 것 같다.

def iscorrect(s):
    stack = []
    st_set = ['(', '{', '[']
    #en_set = [')', '}', ']']
    d = {'(':')', '{':'}', '[':']'}
    count = 0
    
    for c in s:
        if c in st_set:
            stack.append(c)
        elif not stack:
            return 0
        elif c == d[stack[-1]]: # stack이 존재하고, en_set일 때, stack을 제거 가능한 경우
            stack.pop()
            if not stack:
                count += 1
        else:
            return 0
    
    return count if not stack else 0


def solution(s):
    ss = s + s
    slen = len(s)
    for i in range(slen):
        answer = iscorrect(ss[i: i + slen])
        if answer > 0:
            break
    return answer