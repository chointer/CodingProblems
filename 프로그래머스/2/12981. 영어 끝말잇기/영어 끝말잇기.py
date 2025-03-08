# n <= 100
# 1) 끝 문자를 맞추지 않았거나, 2) 이미 나온 단어를 사용하면 끝

def solution(n, words):
    used = set()
    st = None
    for i, word in enumerate(words):
        # 1) 끝 문자 안 맞음 (st가 있는데 st와 맞지않는)
        if st and st != word[0]:
            break
        # 2) 이미 나온 단어
        elif word in used:
            break
        else:
            used.add(word)
            st = word[-1]
    else:
        return [0, 0]
    
    return [i%n + 1, i//n + 1]