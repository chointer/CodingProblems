def facto(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def solution(n, k):
    answer = []
    people = list(range(1, n + 1))
    k -= 1
    
    for i in range(n-1, 0, -1):
        f = facto(i)
        rank = k // f
        k = k % f
        
        num = people[rank]
        answer.append(num)
        people.remove(num)

    answer.append(people.pop())    
    
    return answer