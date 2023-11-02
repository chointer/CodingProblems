# 처음에 뒤로 점프하는 것을 고려했지만, 문제는 고려하지 않는 것 같다.
# 10**4 * 10**4
# 최대 도달 가능 위치만 저장해서 갱신?

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0

        for loc, jump in enumerate(nums):
            if max_pos >= loc:
                max_pos = max(max_pos, loc + jump)
            else:
                break
                
        return True if max_pos >= len(nums) - 1 else False
