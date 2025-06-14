class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        answer = 0
        
        for i in range(N):
            answer = max(abs(nums[i] - nums[(i + 1) % N]), answer)
            
        return answer