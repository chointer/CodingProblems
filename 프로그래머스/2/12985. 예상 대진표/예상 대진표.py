# N = 2**n (1<=n<=20)
def solution(n, a, b):
    match_total = len(bin(n)) - 3
    a = bin(a-1)[2:]
    a = '0' * (match_total - len(a)) + a
    b = bin(b-1)[2:]
    b = '0' * (match_total - len(b)) + b
    print(a,b)    
    
    for i, (digit_a, digit_b) in enumerate(zip(a, b)):
        if digit_a != digit_b:
            break

    return match_total - i