# 40*40 * 4 * 20*20 (?) => 2**8 * 1e4 ~ 1e7 (* 0.25)

def rotate(key):
    K = len(key)
    key_rot = [[0 for _ in range(K)] for _ in range(K)]
    for y in range(K):
        for x in range(K):
            key_rot[x][K-1-y] = key[y][x]
    return key_rot


def compare(key, lock, y0_key, x0_key, E, K, L):
    for y_key in range(K):
        y_loc = y0_key + y_key
        if y_loc < 0 or y_loc >= L:
            continue
            
        for x_key in range(K):
            x_loc = x0_key + x_key
            if x_loc < 0 or x_loc >= L:
                continue
            
            val_key = key[y_key][x_key]
            val_loc = lock[y_loc][x_loc]
            
            if val_key == 1 and val_loc == 0:
                E -= 1
            elif val_key == 0 and val_loc == 1:
                pass
            else:
                return False
    
    return True if E == 0 else False


def solution(key, lock):
    K = len(key); L = len(lock)
    empty = 0
    for line in lock:
        for element in line:
            if element == 0: 
                empty += 1
    
    # rotation
    for rot in range(4):
        # search
        for y0 in range(1-K, L):
            for x0 in range(1-K, L):
                if compare(key, lock, y0, x0, empty, K, L):
                    return True
            
        if rot != 3:
            key = rotate(key)
    
    return False