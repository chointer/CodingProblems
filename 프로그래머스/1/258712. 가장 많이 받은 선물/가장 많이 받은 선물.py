# 선물지수 = 준 선물 - 받은 선물
# friends <= 50, fits <= 1e4
# Counting O(1e4)
# table[i][j]: 친구 i가 친구 j에게 준 선물 수 == 친구 j가 친구 i에게 받은 선물 수

def solution(friends, gifts):
    N_f = len(friends)
    table = [[0 for _ in range(N_f)] for _ in range(N_f)]
    name2idx = {n: i for i, n in enumerate(friends)}
    
    # Count Gifts
    for gift in gifts:
        A, B = map(lambda x: name2idx[x], gift.split())
        table[A][B] += 1
    
    # Calculate Gift Scores
    gift_scores = []
    for i in range(N_f):
        gives = 0
        receives = 0
        for j in range(N_f):
            gives += table[i][j]
            receives += table[j][i]
        gift_scores.append(gives - receives)

    # Predict next month
    max_gift = -1
    
    for i in range(N_f):
        n_to_receive = 0
        for j in range(N_f):
            ij_ji = table[i][j] - table[j][i]
            if ij_ji > 0:
                n_to_receive += 1
            elif ij_ji == 0 and gift_scores[i] > gift_scores[j]:
                n_to_receive += 1
        max_gift = max(max_gift, n_to_receive)
    
    return max_gift