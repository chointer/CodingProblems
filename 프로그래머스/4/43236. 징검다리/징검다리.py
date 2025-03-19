def is_possible(min_dist, rocks, n):
    # min_dist보다 작은 거리를 계속 제거
    past_rock = 0
    for rock in rocks:
        if rock - past_rock < min_dist:
            n -= 1
        else: 
            past_rock = rock
    return False if n < 0 else True
    
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    st = 0
    en = distance + 1
    
    while st <= en:
        mid = (st + en) // 2
        ispossible = is_possible(mid, rocks, n)
        if ispossible:  # min을 만족할 수 있으면, 더 큰 min을 찾는다.
            st = mid + 1
        else:
            en = mid - 1
    return en