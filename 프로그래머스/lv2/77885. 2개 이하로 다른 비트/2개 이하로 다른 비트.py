def f(x):
    xb = list(bin(x))
    del xb[1]
    
    for i in range(len(xb) - 1, -1, -1):
        if xb[i] == '0':
            xb[i] = '1'
            if i != len(xb) - 1:
                xb[i + 1] = '0'
            break
        
    return int("".join(xb), 2)

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number))
    return answer