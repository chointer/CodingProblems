# calcuate the max for each pos.
def solution(land):
    memory = [0, 0, 0, 0]
    for r in land:
        memory_temp = [0, 0, 0, 0]
        for i, now in enumerate(r):
            candi = memory.copy()
            del candi[i]
            memory_temp[i] = max(candi) + now
        memory = memory_temp
        
    return max(memory)