# accumulate에서 min, max gap을 구하면 되려나

def solution(sequence):
    accum = [0]
    
    seq_sum = 0
    pulse = -1
    for i, el in enumerate(sequence):
        seq_sum += pulse**i * el
        accum.append(seq_sum)

    gap = max(accum) - min(accum)
    return gap