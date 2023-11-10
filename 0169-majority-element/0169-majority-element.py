from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_size = len(nums)/2
        counter = Counter(nums)
        return counter.most_common()[0][0]