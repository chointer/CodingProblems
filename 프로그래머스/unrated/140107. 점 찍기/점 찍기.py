def solution(k, d):
    count = 0
    
    for y in range(0, d + 1, k):
        count += 1 + int((d**2 - y**2)**0.5) // k
        
    return count