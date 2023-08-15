def solution(n):
    n = sorted(list(str(n)), reverse=True)
    return int("".join(n))