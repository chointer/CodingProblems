# n <= 10
# 10C5 * 6^5 * 6^5 ~ 1.5e10
# 해설 앞부분을 보니, "효율적인 완전 탐색"을 하라고 한다.
# 6^5개에 대해 순서대로 승패 체크 -> 대략 O(N logN) 스케일?

from itertools import combinations, product

def get_sums(dices):
    result = []
    for p in product(*dices):
        result.append(sum(p))
    return sorted(result)
        
def solution(dice):
    num_of_cases = 6**(len(dice)//2)    
    best_combination = []
    best_wins = 0
    
    for c in combinations(range(len(dice)), len(dice)//2):
        As, Bs = [], []
        for i in range(len(dice)):
            if i in c:
                As.append(dice[i])
            else:
                Bs.append(dice[i])

        Asums = get_sums(As)
        Bsums = get_sums(Bs)
        #print(Asums, '\n', Bsums)
        
        # 기준 number 설정; criterion. 그 값보다 작은 개수, 같은 개수, 큰 개수.
        pre_A = -1
        crit_Bidx = 0
        crit_counts = [0, 0, num_of_cases]
        tot_counts = [0, 0, 0]         # num of Win Draw Lose
        
        for a in Asums:
            if a != pre_A:
                pre_A = a
                crit_counts[0] += crit_counts[1]
                crit_counts[1] = 0
                
            # count crit_counts
            while crit_Bidx < num_of_cases:
                if Bsums[crit_Bidx] < a:
                    crit_counts[0] += 1
                elif Bsums[crit_Bidx] == a:
                    crit_counts[1] += 1
                else:
                    break
                crit_counts[2] -= 1
                crit_Bidx += 1
            
            for i in range(3):
                tot_counts[i] += crit_counts[i]
        
        # compare
        if tot_counts[0] > best_wins:
            best_wins = tot_counts[0]
            best_combination = c
    
    return [i + 1 for i in best_combination]