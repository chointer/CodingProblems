"""
1. 순서대로 하나씩 문자를 체크한다.
    p 혹은 P이면 CountP 1 추가
    y 혹은 Y이면 CountY 1 추가

2. Nump NumY를 비교
    같으면 return True 
    다르면 return False
"""

def solution(s):
    CountP = 0 
    CountY = 0
    
    # 1. 순서대로 하나씩 문자를 체크한다.
    for i in s:
        if i == "p":
            CountP = CountP + 1
        elif i == "P":
            CountP = CountP + 1
        elif i == "y":
            CountY = CountY + 1
        elif i == "Y":
            CountY = CountY + 1
    
    # 2. 비교 및 반환
    if CountP == CountY:
        return True
    else:
        return False