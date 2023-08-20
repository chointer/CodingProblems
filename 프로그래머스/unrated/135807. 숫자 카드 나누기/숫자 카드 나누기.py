# 10**8 -sqrt-> 10**4
# 10**4*10**6 -> 10**10...
# 각 array의 첫 수만 약수를 구하고, 그 약수들에 대해 나머지 체크하는게 더 빠를지도 모르겠다.
def divisor(num):
    answers = []
    for i in range(1, int(num**0.5 + 1)):
        if num%i == 0:
            answers.append(i)
            answers.append(num//i)
    return answers

def solution(arrayA, arrayB):
    A_divs = divisor(arrayA[0])
    B_divs = divisor(arrayB[0])
    
    for A in arrayA:
        for A_div in A_divs.copy():
            if A%A_div != 0:
                A_divs.remove(A_div)
        for B_div in B_divs.copy():
            if A%B_div == 0:
                B_divs.remove(B_div)
                
    for B in arrayB:
        for A_div in A_divs.copy():
            if B%A_div == 0:
                A_divs.remove(A_div)
        for B_div in B_divs.copy():
            if B%B_div != 0:
                B_divs.remove(B_div)
    
    ABs = A_divs + B_divs
    return 0 if not ABs else max(ABs)