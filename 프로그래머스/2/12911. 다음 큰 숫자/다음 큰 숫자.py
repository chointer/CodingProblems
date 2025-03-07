# 이진수 변환 시, 1의 개수가 같은, 바로 다음 큰 수
# n <= 1e6 -> ~20자리 binary?
# 자릿수가 바뀌는 경우는 어떡할까.
# 규칙: (1) "01" 부분을 찾아서 바꾼다. (2) 나머지 작은 숫자자리들로 가장 작은 수를 만든다.

def solution(n):
    nbin = bin(n)[2:][::-1] + "0"
    
    for i in range(len(nbin)-1):
        if nbin[i:i+2] == "10":
            break
    
    left = nbin[:i]
    right = "01" + nbin[i+2:]
    
    n_ones = 0
    for digit in left:
        if digit == '1':
            n_ones += 1
    
    left = "1" * n_ones + "0" * (len(left) - n_ones)
    
    answer = (left + right)[::-1]
    
    return int(answer, 2)