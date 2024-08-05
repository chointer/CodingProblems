
"""
n 번째 피보나치 수를 구하려면,

for i in range(?):    2, 3, ..., n
    f(i) = f(i-2) + f(i-1)
    
f(2) = f(0) + f(1)
f(3) = f(1) + f(2)
f(4) = f(2) + f(3)
...


"""


def solution(n):
    seq = [0, 1]
    
    for i in range(n-1):
        j = i + 2
        value = seq[j-2] + seq[j-1]
        seq.append(value)

    return seq[n]%1234567