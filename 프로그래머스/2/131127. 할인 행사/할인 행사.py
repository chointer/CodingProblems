# N discount <= 1e5, # want <= 10

from collections import Counter
def is_matched(discounts_dict, wants, numbers):
    for want, num in zip(wants, numbers):
        if discounts_dict[want] != num:
            return 0
    return 1
    
def solution(want, number, discount):
    discounts_dict = Counter(discount[:10])
    count_days = is_matched(discounts_dict, want, number)
    
    for disc_in, disc_out in zip(discount[10:], discount[:-10]):
        discounts_dict[disc_out] -= 1
        discounts_dict[disc_in] += 1
        count_days += is_matched(discounts_dict, want, number)
        
    return count_days