# length <= 1e6, phone_length <= 20

def solution(phone_book):
    phone_set = set()
    for phone in phone_book:
        phone_set.add(phone)

    answer = True
    for phone in phone_book:
        temp = ""
        for p in phone:
            temp += p
            if temp in phone_set and temp != phone:
                answer = False
    
    return answer