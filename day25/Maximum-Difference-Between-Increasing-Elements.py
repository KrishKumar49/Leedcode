from typing import List
    
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        minElement = nums[0]
        maxDiff = -1
        
        for j in  range(1, n):
            if nums[j] > minElement:
                diff = nums[j] - minElement
                maxDiff = max(maxDiff, diff)
                
            else:
                minElement = nums[j]
                
        return maxDiff



if __name__ == "__main__":
    nums = [7, 1, 5, 4]
    solution = Solution()
    print(solution.maximumDifference(nums))  
    
    nums = [9, 4, 3, 2]
    print(solution.maximumDifference(nums)) 
    
    nums = [1, 2, 3, 4, 5]
    print(solution.maximumDifference(nums))  