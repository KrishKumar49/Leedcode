class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
    
        return self.bs(nums, left, right, target)

        
    def bs(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return left
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            return self.bs(nums, left, mid-1, target)

        else:
            return self.bs (nums, mid+1, right, target)