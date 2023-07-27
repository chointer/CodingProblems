"""
n번째 칸토어 비트열 Kn은 (n-1)번째 비트열의 반복; K(n+1) = [Kn Kn O Kn Kn] (가운데는 전부 0)
l, r에서 1을 뺀 값을 5진수로 변환하면, 각 자리수는 i번째 비트열에서의 위치를 의미한다.
예시에서 r=17, r-1을 5진수로 변환하면, 31. 
즉, K1에서 3번째 값, K2에서는 K1 부분 비트열에서 1번째 값
Ki에서의 위치까지의 1개수를 구해서 Kn에서 몇 개의 1이 생기는지 계산하고, 이를 반복하면 l과 r까지의 1개수를 구할 수 있고, 두 값의 차이를 통해 l, r 사이의 1 개수를 구한다.
"""

def dec2five(num, base):
    ans = ''

    while num > 0:
        num, mod = divmod(num, base)
        ans += str(mod)    

    return ans[::-1]


def N1(n, loc, lr):
    answer = 0
    
    for i in range(n):
        x = int(loc[i])
        
        # before loc
        if x < 3:
            answer += x * 4**(n-i-1)
        else:
            answer += (x-1) * 4**(n-i-1)
        # loc
        if x == 2:
            return answer
    
    return answer if lr == 'l' else answer + 1
    

def solution(n, l, r):
    l5 = dec2five(l-1, 5).zfill(n)
    r5 = dec2five(r-1, 5).zfill(n)
    
    N1l = N1(n, l5, 'l')
    N1r = N1(n, r5, 'r')
    
    return N1r-N1l