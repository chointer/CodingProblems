# 질문 참고함; lost, reserve 모두 속한 학생은 무조건 자기 여벌을 사용해야하는데, 내가 구현한 코드는 그러지 않았다.

def solution(n, lost, reserve):
    for i in reserve.copy():
        if i in lost:
            lost.remove(i)
            reserve.remove(i)

    for i in sorted(reserve):
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
    return n - len(lost)