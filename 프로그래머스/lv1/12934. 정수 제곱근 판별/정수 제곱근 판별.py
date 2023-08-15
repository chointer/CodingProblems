def solution(n):
    n_sqrt = int(n**0.5)
    return (n_sqrt+1)**2 if n == n_sqrt**2 else -1