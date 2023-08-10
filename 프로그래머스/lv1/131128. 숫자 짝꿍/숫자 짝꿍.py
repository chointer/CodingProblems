from collections import Counter

def solution(X, Y):
    xs = Counter(X)
    ys = Counter(Y)

    ans = []
    for i in range(9, -1, -1):
        i = str(i)
        ans.append(i * min(xs[i], ys[i]))
    answer = ("".join(ans))
    
    if not answer:
        answer = '-1'
    
    if answer[0] == '0':
        answer = '0'
    
    return answer