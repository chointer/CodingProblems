# sort lambda, bitwise XOR
# 20m

def solution(data, col, row_begin, row_end):
    # 1 & 2 (Sorting)
    data.sort(key=lambda x: (x[col-1], -x[0]))

    # 3 S_is
    Si0 = 0
    for i, row in enumerate(data[row_begin - 1: row_end], start=row_begin):
        Si = 0
        for val in row:
            Si += val%i
        Si0 = Si ^ Si0

    return Si0