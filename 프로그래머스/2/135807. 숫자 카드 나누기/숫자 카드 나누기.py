# 정답은 arrayA의 gcd와 arrayB의 gcd만 가능하다?
# arrayA+B <= 1e6
# element <= 1e8

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = arrayA[0]
    for a in arrayA:
        gcdA = gcd(gcdA, a)
    
    for b in arrayB:
        if b%gcdA == 0:
            gcdA = 0
            break
    answer = max(answer, gcdA)    

    
    gcdB = arrayB[0]
    for b in arrayB:
        gcdB = gcd(gcdB, b)
    
    for a in arrayA:
        if a%gcdB == 0:
            gcdB = 0
            break
    answer = max(answer, gcdB)    
    
    return answer