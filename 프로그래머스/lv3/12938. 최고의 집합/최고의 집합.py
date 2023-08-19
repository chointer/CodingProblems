def solution(n, s):
    a = s//n
    b = s%n
    if a == 0: return [-1]
    
    answer = []
    for i in range(n - b):
        answer.append(a)
    for i in range(b):
        answer.append(a + 1)
    return answer