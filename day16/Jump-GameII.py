class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        jump = 0
        farthest = 0
        end = 0

        for i in range(N - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == end:
                jump += 1
                end = farthest
            
        return jump
