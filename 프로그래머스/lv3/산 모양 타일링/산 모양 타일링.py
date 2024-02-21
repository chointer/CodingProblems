# 27m
# DP 같은데.. 마지막이 삼각형인지 마름모인지 구분해두기?
# for i in range(n):
# if Top(i+1):
#   삼(i+1) = 삼(i) * 3  +  마(i) * 2
#   마(i+1) = 삼(i)  +  마(i)
# else:
#   삼(i+1) = 삼(i) * 2  +  마(i)
#   마(i+1) = 삼(i)  +  마(i)

def solution(n, tops):
    # initial condition
    tri = 1
    squ = 0
    
    for top in tops:
        if top:
            tri, squ = tri*3 + squ*2, tri + squ
        else:
            tri, squ = tri*2 + squ, tri + squ
        tri, squ = tri%10007, squ%10007
        
    return (tri + squ)%10007
