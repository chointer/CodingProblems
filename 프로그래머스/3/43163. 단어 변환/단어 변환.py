# 단어 길이 <= 10, 단어 개수 <= 50
# BFS
# link matrix 만들기

from collections import deque
queue = deque()

def is_linked(word1, word2):
    n_dif = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            n_dif += 1
    return True if n_dif == 1 else False

def solution(begin, target, words):
    words.append(begin)
    n = len(words)
    
    # generate map
    maps = [[False for _ in range(n)] for _ in range(n)]
    target_idx = -1
    for idx1, word1 in enumerate(words):
        if word1 == target:
            target_idx = idx1
        for idx2, word2 in enumerate(words):
            if is_linked(word1, word2):
                maps[idx1][idx2] = True
                maps[idx2][idx1] = True
    
    if target_idx == -1:
        return 0
    
    # BFS
    queue.append((n - 1, 0))        # begin index가 n - 1
    while queue:
        idx_word, d = queue.popleft()
        for idx_linked, TF in enumerate(maps[idx_word]):
            if TF:
                if idx_linked == target_idx:
                    return d + 1
                maps[idx_word][idx_linked] = False
                maps[idx_linked][idx_word] = False
                queue.append((idx_linked, d + 1))
    return -1010