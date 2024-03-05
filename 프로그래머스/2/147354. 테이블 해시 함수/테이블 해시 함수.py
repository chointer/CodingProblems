# N <= (2500, 500) ~ 1e6

def solution(data, col, row_begin, row_end):
    data_sort = sorted(data, key = lambda x: (x[col - 1], -x[0]))
    
    answer = 0
    for r in range(row_begin, row_end + 1):
        modes = 0
        for ele in data_sort[r - 1]:
            modes += ele%r
        answer ^= modes
    return answer