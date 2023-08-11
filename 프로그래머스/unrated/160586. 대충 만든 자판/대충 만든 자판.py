# dict {key: min_type}

def solution(keymap, targets):
    # make dict
    dict_key = {}
    for keym in keymap:
        count = 0
        for k in keym:
            count += 1
            if k not in dict_key or dict_key[k] > count:
                dict_key[k] = count
    
    # calcuate targets
    answer = []
    for target in targets:
        count_sum = 0
        for t in target:
            if t in dict_key:
                count_sum += dict_key[t]
            else:
                count_sum = -1
                break
        answer.append(count_sum)
            
    return answer