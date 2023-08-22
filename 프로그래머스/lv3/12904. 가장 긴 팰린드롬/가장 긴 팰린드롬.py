# 단순히, 각 문자기준 양쪽을 체크하면? 2500*2500 = 6250000 < 1e7
# 문자를 기준으로하면 짝수 팰린드롬 확인이 불가능.
# indexing에서 추가 시간이 생기지는 않으려나
# 27m 14s. 

def solution(s):
    answer = 0
    N = len(s)
    s = list(s)
    for i in range(N):
        # odd
        length = min(i, N-1-i)
        s1 = s[i-length:i]
        s2 = s[i+1:i+1+length][::-1]
    
        pal = 1
        for _ in range(length):
            if s1.pop() == s2.pop():
                pal += 2
            else:
                break
        answer = max(answer, pal)
        
        
        # even
        length = min(i+1, N-1-i)
        s1 = s[i+1-length:i+1]
        s2 = s[i+1:i+1+length][::-1]
    
        pal = 0
        for _ in range(length):
            if s1.pop() == s2.pop():
                pal += 2
            else:
                break
        
        answer = max(answer, pal)
        
    return answer