# O(N) <= 5,000 * sqrt(N) <= 5,000 * 10**(9/2) < 10**(4+5)
# (10,000,000보다 작은) 약수 중 가장 큰 수

def max_div(n):
    if n == 1:
        return 0
    
    max_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            max_div = max(max_div, i)
            div = n//i
            if div <= 10000000:
                max_div = max(max_div, div)
    
    return max_div

    
def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(max_div(i))
        
    return answer