# N <= 2*1e8
# stations <= 1e4
# 각 station 사이의 거리 - 2W.를 (2W+1)로 나누기
# 15m 33s. 1씩 차이 나는 부분이 있어서 어려웠다.

def solution(n, stations, w):
    stations = [-w] + stations + [n+w+1]
    
    wave_range = 2*w+1
    count = 0
    
    for s1, s2 in zip(stations[:-1], stations[1:]):
        l = s2 - s1 - wave_range
        
        if l <= 0: 
            continue
        
        count += l//wave_range
        if l%wave_range:
            count += 1
    
    return count