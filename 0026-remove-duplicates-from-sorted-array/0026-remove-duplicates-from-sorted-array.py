# length < 3 * 10**4

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numset = set(nums)
        nums_unique = sorted(list(numset))
        N = len(numset)
        
        for i in range(N):
            nums[i] = nums_unique[i]
            
        return N