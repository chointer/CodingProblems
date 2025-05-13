# N <= 1000
from functools import cmp_to_key

def cmp(a, b):
    ab = a + b
    ba = b + a
    
    if ab > ba:
        return -1
    elif ab < ba:
        return 1
    else:
        return 0
    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(cmp))
    
    answer = "".join(numbers)
    
    return "0" if answer[0] == '0' else answer
    
    


'''
def solution(numbers):
    # N = 1
    if len(numbers) == 1:
        return str(numbers[0])
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x * 4, reverse=True)

    return str(int("".join(numbers)))
'''