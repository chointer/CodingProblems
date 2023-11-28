# 마지막 idx에 도달하기 위한 최소 jump 횟수
# N <= 1e4
# 비슷한 문제에서 거꾸로 생각하라고 했던 거 같은데 with DP 
# -> 뒷 위치부터, 마지막 위치에 도달하기 위한 최소 jump 수

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        n_jumps = [100000 for i in range(length)]
        n_jumps[0] = -1
        nums = nums[::-1]

        for idx, val in enumerate(nums):
            n_jumps[idx] = min(n_jumps[max(0, idx - val):(idx + 1)]) + 1
            
        return n_jumps[-1]