# 1e6 * 20 = 2e7
# 긴 것부터 트리 구조? O(N) = NlogN + N*L
# root: (n, dict)

def solution(phone_book):
    root = {}
    phone_book.sort(key=lambda x: len(x), reverse=True)
    
    for phone in phone_book:
        pointer = root
        
        for p in phone:
            if p not in pointer:
                pointer[p] = {}
            pointer = pointer[p]
            
        if len(pointer) != 0:
            return False
        
    return True
    
"""
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        a = phone_book[i]
        b = phone_book[i + 1]
        Na = len(a)
        Nb = len(b)
        if Na < Nb:
            if a == b[:Na]:
                return False
    return True
"""
"""
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
"""