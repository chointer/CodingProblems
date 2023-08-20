def solution(r1, r2):
    count = 0
    
    for y in range(r2):
        # x_max
        x_max = int((r2**2 - y**2)**0.5)
        
        # x_min
        if y <= r1:
            x_min = (r1**2 - y**2)**0.5
            if x_min < 1:
                x_min = 1
            elif x_min - int(x_min) > 0:
                x_min = int(x_min) + 1
            else:
                x_min = int(x_min)
        else:
            x_min = 1
        
        count += x_max - x_min + 1
        
    return count * 4