def solution(n):
    fi0, fi1 = 1, 1
    
    for i in range(n - 2):
        fi0, fi1 = fi1, (fi0 + fi1)%1234567
    
    return fi1