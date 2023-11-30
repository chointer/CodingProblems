# m, n <= 100
# 본인 기준, 위 & 왼쪽 값을 알고 있는 격자를 계산할 수 있다.

from collections import defaultdict

def solution(m, n, puddles):
    lis = [(i, j) for i in range(m) for j in range(n)]
    lis.sort(key=lambda x: sum(x))
    lis.remove((0, 0))
    for px, py in puddles:
        lis.remove((px-1, py-1))

    paths = defaultdict(int)
    paths[(0, 0)] = 1
    
    for loc in lis:
        paths[loc] = (paths[(loc[0]-1, loc[1])] + paths[loc[0], loc[1]-1])%1000000007
    
    return paths[(m-1, n-1)]