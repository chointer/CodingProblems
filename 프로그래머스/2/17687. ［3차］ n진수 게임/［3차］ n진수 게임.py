# t * m <= 1e5

def dec2base(num, base):
    if num == 0: return "0"
    result = ""
    numbers = "0123456789ABCDEF"
    while num > 0:
        num, i = num//base, num%base
        result += numbers[i]
    return result[::-1]

def solution(n, t, m, p):
    N_to_calculate = t * m
    number_list = ""
    number_in_10 = 0
    
    while len(number_list) < N_to_calculate:
        number_list += dec2base(number_in_10, n)
        number_in_10 += 1
    
    answer = ''
    p -= 1
    for i in range(t):
        answer += number_list[i * m + p]
    return answer