# 3*10**4
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_alloc = 0
        last_val = -10000000
        flag_pass = False
        
        for p_check in range(len(nums)):
            val = nums[p_check]

            if flag_pass:
                if last_val == val:
                    continue
                else:
                    flag_pass = False
            
            if last_val == val:
                flag_pass = True

            nums[p_alloc] = val
            p_alloc += 1
            last_val = val
        
        return p_alloc