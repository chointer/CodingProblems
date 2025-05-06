from collections import Counter
def solution(nums):
    answer = min(len(nums)//2, len(Counter(nums)))
    return answer


"""
def solution(nums):
    species = set(nums)
    n_species = len(species)
    n_take = int(len(nums)/2)
    if n_species <= n_take:
        answer = n_species
    else:
        answer = n_take
    return answer
"""