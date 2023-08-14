# 가장 높은 10의 자리 수에서 내려가는 방향만 고려하도록 해서 틀림.
def solution(storey):
    floors = [(storey, 0)]       # (floor, used stones)
    record = sum(map(int, list(str(storey))))

    while floors:
        floor, used = floors.pop()
        
        if used > record: 
            continue
        
        if floor == 0:
            record = min(record, used)
            continue
        
        n = floor%10    # digit of this rank
        
        # up
        up = 10 - n
        floors.append(((floor + up)//10, used + up))

        # down
        floors.append(((floor - n)//10, used + n))

    return record