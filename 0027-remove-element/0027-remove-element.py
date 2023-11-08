class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        st = 0
        en = len(nums) - 1
        
        while st < en:
            if nums[en] == val:
                en -= 1
            
            elif nums[st] != val:
                st += 1
            
            else:   # nums[st] == val
                nums[st], nums[en] = nums[en], nums[st]
        
        return st if nums[st] == val else st + 1
            