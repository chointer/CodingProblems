# height <= 500
# n-th sum 구할 때, (n-1)th sum에서 둘 중 큰 것을 선택한다.
# n층 i번째의 summ은 n-1층 max(summ(i-1), summ(i))

def solution(triangle):
    sums = [0]
    for floor in triangle:
        new_sums = []
        n = len(floor)
        for i, el in enumerate(floor):
            if i == 0:
                new_sums.append(sums[0] + el)
            elif i == n - 1:
                new_sums.append(sums[i - 1] + el)
            else:
                new_sums.append(max(sums[i - 1], sums[i]) + el)
        sums = new_sums
    return max(sums)