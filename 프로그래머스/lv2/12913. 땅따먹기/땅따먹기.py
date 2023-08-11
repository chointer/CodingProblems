# remember 1st and 2nd plans and their final positions
# list.index(value), list.pop(idx)

def find(row):
    row_sort = sorted(row, reverse=True)
    val1 = row_sort[0]
    val2 = row_sort[1]
    val3 = row_sort[2]
    pos1, pos2, pos3 = -1, -1, -1
    
    for i, num in enumerate(row):
        if pos1 == -1 and num == val1: pos1 = i
        elif pos2 == -1 and num == val2: pos2 = i
        elif num == val3: pos3 = i
    
    return val1, pos1, val2, pos2, val3, pos3


def solution(land):
    """
    t_val1, t_pos1, t_val2, t_pos2, t_val3, t_pos3 = find(land.pop(0))
    
    for r in land:
        val1, pos1, val2, pos2, val3, pos3 = find(r)
        if t_pos1 != pos1:
            # for 2nd
            candidates = []
            if t_pos1 != pos2: candidates.append((t_val1 + val2, pos2))
            if t_pos2 != pos2: candidates.append((t_val2 + val2, pos2))
            if t_pos1 != pos3: candidates.append((t_val1 + val3, pos3))
            t_val1 += val1
            t_pos1 = pos1
            t_val2, t_pos2 = max(candidates)
        else:
            # 1st
            candidates = [(t_val1 + val2, pos2), (t_val2 + val1, pos1)]
            candidates.sort(reverse=True)
            t_val1, t_pos1 = candidates[0]
            t_val2, t_pos2 = candidates[1]
    """
    memory = [0, 0, 0, 0]
    for r in land:
        memory_temp = [0, 0, 0, 0]
        for i, now in enumerate(r):
            candi = memory.copy()
            del candi[i]
            memory_temp[i] = max(candi) + now
        memory = memory_temp
        
    return max(memory)