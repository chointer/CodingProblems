# 1,000개 직선의 교점 -> 10**3 * 10**3 = 1e6
# 25m 30s

def point(l1, l2):
    A, B, E = l1
    C, D, F = l2
    ADBC = A*D - B*C
    if ADBC == 0:
        return (0, 0), False
    else:
        x = (B*F - E*D)/ADBC
        y = (E*C - A*F)/ADBC
        if x-int(x) != 0 or y-int(y) != 0:
            return (0, 0), False
        else:
            return (int(x), int(y)), True

    
def solution(line):
    # Find Intersections
    dots = []
    for i, l1 in enumerate(line):
        for l2 in line[i+1:]:
            pos, TF = point(l1, l2)
            if TF is True:
                dots.append(pos)

    # Draw Map
    dots_sort_x = sorted(dots)
    dots_sort_y = sorted(dots, key=lambda x: x[1])
    
    x_min = dots_sort_x[0][0]
    x_max = dots_sort_x[-1][0]
    y_min = dots_sort_y[0][1]
    y_max = dots_sort_y[-1][1]
    
    answer = [['.' for _ in range(x_max - x_min + 1)] for _ in range(y_max - y_min + 1)]
    
    # Draw Stars
    for x, y in dots:
        x -= x_min
        y = -(y - y_min) -1
        answer[y][x] = '*'
    
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
        
    return answer