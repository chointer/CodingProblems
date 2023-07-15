def solution(elements):
    # 1-length
    sums = set(elements)
    sum_list = elements.copy()
    N = len(elements)
    
    for i in range(1, N):
        # add
        sum_list_new = []
        for idx in range(N):
            sum_list_new.append(sum_list[idx] + elements[(idx + i) % N])
        sum_list = sum_list_new
        sums.update(sum_list)
        
    return len(sums)