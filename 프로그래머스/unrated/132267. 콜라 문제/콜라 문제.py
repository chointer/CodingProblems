def solution(a, b, n):
    count = 0
    while n >= a:
        get = (n//a) * b
        n = get + n%a
        count += get
        
    return count