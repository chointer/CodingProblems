# arr <= 15

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

def solution(arr):
    
    result = 1

    for a in arr:
        result = lcm(result, a)
    return result