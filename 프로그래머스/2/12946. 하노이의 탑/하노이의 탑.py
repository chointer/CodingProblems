# 1) n-1까지의 판을 (2)로 이동
# 2) n 판을 (3)으로 이동
# 3) n-1까지의 판을 (3)으로 이동
# => DP?

def get_path(st, en, mid, path):
    columns = (st, en, mid)
    answer = []
    for p in path:
        answer.append(
            [columns[p[0]], columns[p[1]]]
        )
    return answer

def solution(n):
    ST, EN, MID = 0, 1, 2
    paths = {1: [[ST, EN]]}
    
    if n == 1:
        return get_path(1, 3, 2, paths[1])
    
    for i in range(2, n + 1):
        paths[i] = get_path(ST, MID, EN, paths[i-1])
        paths[i].append([ST, EN])
        paths[i] += get_path(MID, EN, ST, paths[i-1])
    return get_path(1, 3, 2, paths[i])