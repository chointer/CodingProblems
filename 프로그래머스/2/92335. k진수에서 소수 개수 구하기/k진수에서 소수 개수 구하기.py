# n <= 1e6

def dec2base(n, k):
    answer = ""
    digits = "0123456789"
    while n > 0:
        n, a = n//k, n%k
        answer += digits[a]
    return answer[::-1]
                   
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

def solution(n, k):
    converted = dec2base(n, k)
    candidates = converted.split("0")
    
    count = 0
    for c in candidates:
        if c and int(c) > 1:
            if is_prime(int(c)):
                count += 1
    
    return count