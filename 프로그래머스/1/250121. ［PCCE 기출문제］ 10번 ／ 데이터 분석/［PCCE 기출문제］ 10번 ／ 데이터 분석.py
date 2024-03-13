# SQL?
# N <= 500

def solution(data, ext, val_ext, sort_by):
    key2idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    extidx = key2idx[ext]
    sortidx = key2idx[sort_by]
    answer = []
    
    for d in data:
        print(d)
        if d[extidx] < val_ext:
            answer.append(d)

    answer.sort(key=lambda x: x[sortidx])

    return answer