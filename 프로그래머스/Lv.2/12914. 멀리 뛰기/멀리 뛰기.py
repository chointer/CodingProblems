# DP.
# f(n) = f(n-1) + f(n-2) ?

def solution(n):
    f = []
    for i in range(n):
        if i == 0:
            f.append(1)
        elif i == 1:
            f.append(2)
        else:
            f.append((f[i-1] + f[i-2])%1234567)
    
    return f[-1]