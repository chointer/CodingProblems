# LRU: 가장 오랫동안 참조되지 않은 페이지를 교체한다.
# 캐시에 해당 데이터가 있으면 cache hit, 없어서 가져와야한다면 cache miss
# 캐시가 비어있으면 stack
# 꽉 차면 가장 오랫동안 참조되지 않은 페이지 제거 후 stack
# 캐시에 있는 데이터를 참조하면, 해당 데이터의 순서 재설정
# N <= 1e5, cache <= 30 => O(30 * 30 * 1e5); 원소 확인 * 원소 삭제 * 도시 수

from collections import deque
def solution(cacheSize, cities):
    cache = deque([], maxlen=cacheSize)
    t = 0
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            t += 1
        else:
            t += 5
            cache.append(city)
    
    return t