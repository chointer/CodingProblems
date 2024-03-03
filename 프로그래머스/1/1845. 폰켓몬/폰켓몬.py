# N <= 1e4, id <= 2e5
def solution(nums):
    N_species = len(set(nums))
    return min(len(nums)//2, N_species)