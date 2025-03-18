from itertools import product
def solution(numbers, target):
    count = 0
    for opers in product(*[[1, -1] for _ in range(len(numbers))]):
        temp_sum = 0
        for oper, num in zip(opers, numbers):
            temp_sum += oper * num
        if temp_sum == target:
            count += 1
            
    return count