# 10**3 simple sort
from collections import deque

def split_file(f):
    result = f
    f = deque(f)
    
    head = []
    number = []
    tail = []
    
    while f and not f[0].isdigit():
        head.append(f.popleft())
    while f and f[0].isdigit():
        number.append(f.popleft())
    
    return ["".join(head), "".join(number), result]
        
    
def compare_files(f1_list, f2_list):
    f1_head, f1_number, _ = f1_list
    f2_head, f2_number, _ = f2_list
    
    # head
    f1_head_lo = f1_head.lower()
    f2_head_lo = f2_head.lower()
    
    if f1_head_lo < f2_head_lo: return 1
    elif f1_head_lo > f2_head_lo: return -1

    # number
    f1_number_n = int(f1_number)
    f2_number_n = int(f2_number)
    
    if f1_number_n < f2_number_n: return 1
    elif f1_number_n > f2_number_n: return -1
    else: return 0


def solution(files):
    N_of_files = len(files)
    answer = []
    for f in files:
        answer.append(split_file(f))

    for i in range(N_of_files):
        for j in range(N_of_files-1):
            sign = compare_files(answer[j], answer[j+1])
            if sign == -1:
                answer[j], answer[j+1] = answer[j+1], answer[j]
    return [ans[2] for ans in answer]