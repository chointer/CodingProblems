# MERGED 구현? union-find?
# 기준 cell에는 내용을 넣고 merged된 셀 위치 리스트
# 나머지 cells에는 기준 셀 위치만

# table_body
# table_parent
# dict_merged = {parent: {child, ...}}

# MERGE에서 "if pr1 == pr2 and pc1 == pc2:"를 안넣었다가 틀렸다.

def Find(r, c, table_parent):
    if table_parent[r][c] == (r, c):
        return (r, c)
    
    table_parent[r][c] = Find(table_parent[r][c][0], table_parent[r][c][1], table_parent)
    return table_parent[r][c]
    
    
def UPDATE(cmd_body, table_body, table_parent):
    if len(cmd_body) == 3:          # UPDATE r c value
        r, c, val = cmd_body
        pr, pc = Find(int(r), int(c), table_parent)
        table_body[pr][pc] = val
    
    else:
        v1, v2 = cmd_body
        for r in range(len(table_body)):
            for c in range(len(table_body[0])):
                pr, pc = Find(r, c, table_parent)
                if table_body[pr][pc] == v1:
                    table_body[pr][pc] = v2

                    
def MERGE(cmd_body, table_body, table_parent, dict_merge):
    r1, c1, r2, c2 = map(int, cmd_body)
    if r1 == r2 and c1 == c2: 
        return
    
    pr1, pc1 = Find(r1, c1, table_parent)
    pr2, pc2 = Find(r2, c2, table_parent)
    if pr1 == pr2 and pc1 == pc2:   ##############################################
        return
    
    # Body Merge
    body1 = table_body[pr1][pc1]
    body2 = table_body[pr2][pc2]
    if body1:
        table_body[pr2][pc2] = ""
    else:
        table_body[pr1][pc1] = body2
        table_body[pr2][pc2] = ""
    
    # Parent Merge
    table_parent[pr2][pc2] = (pr1, pc1)
            
    # Update dict_merge
    if (pr1, pc1) not in dict_merge:
        dict_merge[(pr1, pc1)] = set()
        dict_merge[(pr1, pc1)].add((pr1, pc1))
    
    if (pr2, pc2) in dict_merge:
        dict_merge[(pr1, pc1)].update(dict_merge[(pr2, pc2)])
        del dict_merge[(pr2, pc2)]
    else:
        dict_merge[(pr1, pc1)].add((pr2, pc2))

    
def UNMERGE(cmd_body, table_body, table_parent, dict_merge):
    r, c = map(int, cmd_body)
    pr, pc = Find(r, c, table_parent)
    
    body = table_body[pr][pc]
    
    if (pr, pc) not in dict_merge:
        return
    
    for rr, cc in dict_merge[(pr, pc)]:
        table_body[rr][cc] = ""
        table_parent[rr][cc] = (rr, cc)
    table_body[r][c] = body
    
    del dict_merge[(pr, pc)]
    
    
def PRINT(cmd_body, table_body, table_parent):
    r, c = map(int, cmd_body)
    pr, pc = Find(r, c, table_parent)
    return table_body[pr][pc] if table_body[pr][pc] else "EMPTY"


def solution(commands):
    w, h = 51, 51
    table_body = [["" for _ in range(w)] for _ in range(h)]
    table_parent = [[(r, c) for c in range(w)] for r in range(h)]
    dict_merge = {}
    
    answer = []
    for command in commands:
        command = command.split()
        cmd_head, cmd_body = command[0], command[1:]
        if cmd_head == "UPDATE":
            UPDATE(cmd_body, table_body, table_parent)
        elif cmd_head == "PRINT":
            answer.append(PRINT(cmd_body, table_body, table_parent))
        elif cmd_head == "MERGE":
            MERGE(cmd_body, table_body, table_parent, dict_merge)
        elif cmd_head == "UNMERGE":
            UNMERGE(cmd_body, table_body, table_parent, dict_merge)
    
    """
    for a in range(h):
        print(table_body[a])
    for a in range(h):
        print(table_parent[a])
    """
    return answer