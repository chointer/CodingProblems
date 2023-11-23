from functools import cmp_to_key

def func(x, y):
    xy = int(x + y)
    yx = int(y + x)
    if xy >= yx:
        return -1
    else:
        return 1
    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(func))
    
    if numbers[0] == '0':
        return "0"
    
    return "".join(numbers)