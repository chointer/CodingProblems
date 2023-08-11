from collections import Counter

def quad(arr, x1, x2, y1, y2):
    length = x2 - x1
    length_half = length//2
    Sum = 0
    
    for y in range(y1, y2):
        Sum += sum(arr[y][x1:x2])
    
    if Sum == 0: return Counter([0])
    elif Sum == length ** 2: return Counter([1])
    else: 
        return quad(arr, x1, x1 + length_half, y1, y1 + length_half) + \
                quad(arr, x1 + length_half, x2, y1, y1 + length_half) + \
                quad(arr, x1, x1 + length_half, y1 + length_half, y2) + \
                quad(arr, x1 + length_half, x2, y1 + length_half, y2)
    
def solution(arr):
    N = len(arr)
    result = quad(arr, 0, N, 0, N)
    return [result[0], result[1]]