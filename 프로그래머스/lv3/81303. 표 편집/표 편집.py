# linked list를 구현했지만 적은 개수의 테스트에서 시간초과 및 실패가 있었다.
# 해결하지 못해서 구글 참고해서, 완전 새로 구현했다. 
# 가장 큰 차이점은 answer list를 cmd 수행 중에 지속적으로 갱신한 것이다. 이전에는 cmd를 모두 수행한 다음에 answer list를 만들었다.

def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    tab = {i: [i - 1, i + 1] for i in range(n)}
    tab[0][0] = None
    tab[n-1][1] = None
    erased = []
    
    for c in cmd:
        if c[0] == "U":
            for i in range(int(c[2:])):
                k = tab[k][0]
        elif c[0] == "D":
            for i in range(int(c[2:])):
                k = tab[k][1]
        
        elif c == 'C':
            pre, post = tab[k]
            if pre != None:
                tab[pre][1] = post
            if post != None:
                tab[post][0] = pre
            
            answer[k] = 'X'
            erased.append(k)
            if post == None:
                k = pre
            else:
                k = post
        
        else:   # "Z"
            restore = erased.pop()
            answer[restore] = 'O'
            pre, post = tab[restore]
            if pre != None:
                tab[pre][1] = restore
            if post != None:
                tab[post][0] = restore
    
    return "".join(answer)