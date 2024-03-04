# N <= 7
def dfs(current, left, number_set):
    for n in left.copy():
        number_set.add(int(current + n))
        left.remove(n)
        dfs(current + n, left, number_set)
        left.append(n)

        
def is_prime(n):
    if n < 2: 
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    
    return True

    
def solution(numbers):
    number_set = set()
    numbers = list(numbers)
    
    for num in numbers.copy():
        if num != 0:
            number_set.add(int(num))
            numbers.remove(num)
            dfs(num, numbers, number_set)
            numbers.append(num)

    count = 0
    for n in list(number_set):
        if is_prime(n):
            count += 1
    
    return count