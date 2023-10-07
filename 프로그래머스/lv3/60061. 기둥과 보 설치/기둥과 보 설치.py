# n in [5, 100]
# bulid_frame <= 1000
# [x, y, 종류, 설치삭제], (x, y) 기준 오른쪽/위쪽으로 설치/삭제
# return은 오름차순 (x, y, a)
# 설치/삭제하는 구조물과 인접한 구조물들에 대한 상태 체크
# set 자료구조 활용

from collections import defaultdict

def check_col(x, y, structs):
    if y == 0: return True
    elif (x, y, 1) in structs:
        return True
    elif (x - 1, y, 1) in structs:
        return True
    elif (x, y - 1, 0) in structs:
        return True
    else:
        return False

def check_beam(x, y, structs):
    if (x, y - 1, 0) in structs or (x + 1, y - 1, 0) in structs:
        return True
    elif (x - 1, y, 1) in structs and (x + 1, y, 1) in structs:
        return True
    else: 
        return False
    
def solution(n, build_frame):
    structs = set()                 # (x, y, a): 

    for x, y, typ, act in build_frame:
        # 설치
        if act == 1:                ## Column
            if typ == 0:
                if check_col(x, y, structs):
                    structs.add((x, y, typ))
            else:                   ## Beam
                if check_beam(x, y, structs):
                    structs.add((x, y, typ))
        # 제거
        else:
            structs.remove((x, y, typ))
            if typ == 0:            ## Column
                if (x, y + 1, 0) in structs and not check_col(x, y + 1, structs):
                    structs.add((x, y, typ))
                elif (x, y + 1, 1) in structs and not check_beam(x, y + 1, structs):
                    structs.add((x, y, typ))
                elif (x - 1, y + 1, 1) in structs and not check_beam(x - 1, y + 1, structs):
                    structs.add((x, y, typ))
                else:
                    continue
                    
            else:                   ## Beam
                if (x - 1, y, 1) in structs and not check_beam(x - 1, y, structs):
                    structs.add((x, y, typ))
                elif (x + 1, y, 1) in structs and not check_beam(x + 1, y, structs):
                    structs.add((x, y, typ))
                elif (x, y, 0) in structs and not check_col(x, y, structs):
                    structs.add((x, y, typ))
                elif (x + 1, y, 0) in structs and not check_col(x + 1, y, structs):
                    structs.add((x, y, typ))
                else:
                    continue
                    
    answer = sorted(structs)
    return answer