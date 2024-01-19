# r <= 1e6
import math

def getX(r, y) -> float:
    return 0 if r <= y else (r**2 - y**2)**0.5

def solution(r1, r2):
    N_quarter = 0
    for y in range(1, r2 + 1):
        x2 = int(getX(r2, y))
        x1 = math.ceil(getX(r1, y))
        N_quarter += x2 - x1 + 1
    
    return N_quarter * 4