# 예외 1) 코너 활용, 2) 경로에 공(수직, 수평)
# 37m 30s

def subsol(x_st, y_st, x_en, y_en, m, n, maxl):
    result = maxl
    
    # Vertical
    if x_st == x_en:
        if y_st < y_en:
            result = min(result, (y_st + y_en)**2)
        else:
            result = min(result, (2 * n - y_st - y_en)**2)
    else:
        result = min(result, (x_st - x_en)**2 + (y_st + y_en)**2)
        result = min(result, (x_st - x_en)**2 + (2 * n - y_st - y_en)**2)
    
    # Horizontal
    if y_st == y_en:
        if x_st < x_en:
            result = min(result, (x_st + x_en)**2)
        else:
            result = min(result, (2 * m - x_st - x_en)**2)
    else:
        result = min(result, (y_st - y_en)**2 + (x_st + x_en)**2)
        result = min(result, (y_st - y_en)**2 + (2 * m - x_st - x_en)**2)
        
    # Corner. slope check
    corners = [(0, 0), (m, 0), (0, n), (m, n)]
    for xc, yc in corners:
        L_s_c = (xc-x_st) ** 2 + (yc-y_st) ** 2
        L_c_e = (xc-x_en) ** 2 + (yc-y_en) ** 2
        if L_s_c < L_c_e and (xc-x_en) * (yc-y_st) == (yc-y_en) * (xc-x_st):
            result = min(result, L_s_c + L_c_e)
    
    return result
            
def solution(m, n, startX, startY, balls):
    maxl = m**2 + n**2
    answer = []
    for x_en, y_en in balls:
        answer.append(subsol(startX, startY, x_en, y_en, m, n, maxl))
    return answer