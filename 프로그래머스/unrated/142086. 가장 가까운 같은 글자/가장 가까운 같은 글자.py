def solution(s):
    char_dict = {}
    answer = []

    for i, c in enumerate(s):
        if c not in char_dict.keys():
            answer.append(-1)
        else:
            answer.append(i - char_dict[c])
        char_dict[c] = i
        
    return answer