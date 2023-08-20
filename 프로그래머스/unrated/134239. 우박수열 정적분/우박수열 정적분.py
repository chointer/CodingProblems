# 적분을 여러 번 해야하므로 미리 0부터 모든 구역까지의 적분을 해두는 것이 빠를 것 같다.
def Collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return n*3 + 1
    
def solution(k, ranges):
    # cal integrations
    integs = [0]
    while k != 1:
        k_next = Collatz(k)
        area_k = (k_next + k)/2
        #if (k_next + k)%2 == 1: area_k += 0.5
        integs.append(integs[-1] + area_k)
        k = k_next
    
    # cal results
    length = len(integs) - 1
    answer = []
    
    for a, b in ranges:
        b = length + b
        if a > b:
            answer.append(-1.0)
        else:
            answer.append(integs[b] - integs[a])
    
    return answer